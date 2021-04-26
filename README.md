Installation :

1.Create virtual environment and install all of the requirements, for pyaudio use "pip install .\PyAudio-0.2.11-cp39-cp39-win_amd64.whl"

2.Run findinput.py and locate your recording device and remember their index id

3.Run "main.py"

4.Input your index id you got from (2) to "Device index id" field when running "main.py"

Note1 : If your "StudioMix" (Index 2) doesn't pick up any sound, try to set the default device to SteroMix and its output to speaker, then plug your headphone jack into it
Note2 : PyAudio doesn't seem to be working with Linux, waiting for the dev to fix them then I can re-relese the linux version of the translator

