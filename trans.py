import os, pyaudio, wave, ctypes, json
import speech_recognition as sr
from googletrans import Translator


def pt():
    print("")
    print("")

pt()
choose = input("Do you want to list your SteroMix index id? (yes, no, all) : ")
pt()

if choose == "yes" or choose == "y":
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if (dev['name'][:10] == "Stereo Mix"):
            dev_index = str(dev['index'])
            print(dev_index + " - " + "Stereo Mix")
    pt()
elif choose == "all" or choose == "a":
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        dev_index = str(dev['index'])
        dev_channels = str(dev['maxInputChannels'])
        print("Index " + dev_index + " | Input channels - " + dev_channels + " | " + dev['name'])
    pt()

print("------------------ Holotranslator v1.1 by Gusbell ------------------")
pt()
print("Note : Time between each translation should always be 10 or the webpage might not refresh correctly")
pt()

id = input("Your device index id (default : 1) : ")
channels = input("Your audio channels (default : 2) : ")
time = input("Time between each translation (default : 10s) : ")

check = os.path.isfile("holotrans-output.wav")
check2 = os.path.isfile("jp.txt")

if check == True:
    os.remove("holotrans-output.wav")

if check2 == False:
    with open('jp.txt', 'w', encoding='utf-8') as j:
        with open('en.txt', 'w', encoding='utf-8') as e:
            json.dump("", j)
            json.dump("", e)

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
    WAVE_OUTPUT_FILENAME = "holotrans-output.wav"

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=INDEX,
                    frames_per_buffer=CHUNK)
    
    pt()

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

def trans():
    with open('jp.txt', 'w', encoding='utf-8') as j:
        with open('en.txt', 'w', encoding='utf-8') as e:
            with sr.WavFile("holotrans-output.wav") as source:
                r = sr.Recognizer()
                translator = Translator()
                r.adjust_for_ambient_noise(source)
                audio = r.record(source)
                try:
                    output = r.recognize_google(audio, language="ja-JP")
                    print(output)
                    translation = translator.translate(output, dest="en")
                    print(f"{translation.text}")
                    json.dump(output, j, ensure_ascii=False, indent=4)
                    json.dump(translation.text, e, ensure_ascii=False, indent=4)
                except LookupError:
                    print("Could not understand audio")
                except sr.UnknownValueError:
                    print("No speech detected")

os.startfile("web.exe")
os.startfile("startweb.bat")
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

def run():
    rec()
    trans()
    os.remove("holotrans-output.wav")

while True:
    run()

