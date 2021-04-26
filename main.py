import os
import pyaudio
import wave
import ctypes
import speech_recognition as sr
from googletrans import Translator

print("")
print("------------- Holotranslator v1.0 by Gusbell -------------")
print("")
print("")

id = input("Your device index id (default:1) : ")
channels = input("Your audio channels (default:2) : ")
time = input("Time between each translation (default:10s) : ")

if id == "":
    id = 1
if channels == "":
    channels = 2
if time == "":
    time = 10

def rec():
    FORMAT = pyaudio.paInt16
    CHANNELS = int(channels)
    RATE = 44100
    INDEX = int(id)
    CHUNK = 1024
    RECORD_SECONDS = float(time)
    WAVE_OUTPUT_FILENAME = "holo-output.wav"

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=INDEX,
                    frames_per_buffer=CHUNK)

    print("")
    print("")
    
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def sethidden():
    ctypes.windll.kernel32.SetFileAttributesW("./holo-output.wav", 2)

r = sr.Recognizer()
translator = Translator()

def trans():
    with sr.WavFile("./holo-output.wav") as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        try:
            output = r.recognize_google(audio, language="ja-JP")
            print(output)
            translation = translator.translate(output, dest="en")
            print(f"{translation.text}")
        except LookupError:
            print("Could not understand audio")
        except sr.UnknownValueError:
            print("No speech detected")

def run():
    rec()
    sethidden()
    trans()
    os.remove("holo-output.wav")

while True:
    run()
