import os
import pyaudio
import wave
import speech_recognition as sr
from googletrans import Translator

print("----- Holotranslator Ver1.1 by Gusbell -----")

def rec():
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=1,
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

r = sr.Recognizer()
translator = Translator()

def trans():
    with sr.WavFile("./output.wav") as source:
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
    trans()
    os.remove("output.wav")

while True:
    run()
