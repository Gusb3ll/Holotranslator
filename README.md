Installation :

1.Create virtual environment and install all of the requirements, for pyaudio use "pip install .\PyAudio-0.2.11-cp39-cp39-win_amd64.whl"

2.Run findinput.py and locate your "SteroMix" or your recording device and remember their index id

3.Edit "input_device_index" in "main.py" to your SteroMix id or your recording device id from (2)

4.Run "main.py"

Note : PyAudio doesn't seem to be working with Linux, waiting for the dev to fix them then I can re-relese the linux version of the translator
Note2 : If your "StudioMix" doesn't pick up any sound, try to set the default device to SteroMix and its output, then plug your headphone jack into it
