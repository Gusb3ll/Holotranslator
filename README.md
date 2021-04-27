Installation :

1.Create virtual environment and install all of the requirements, for pyaudio use "pip install .\PyAudio-0.2.11-cp39-cp39-win_amd64.whl"

2.Run "main.py" and type "yes" into the console to display your SteroMix index id (Recommend for first time user), or "all" if you want to list all device and it's index id

3.Input your first SteroMix index id into the console when asked to

4.Adjust the channels of your input device (SteroMix default is 2)

5.Adjust the time between each translation and you're good to go!

Note1 : If your "StudioMix" doesn't pick up any sound, try to set the default device to SteroMix and its output to speaker, then plug your headphone jack into it
Note2 : PyAudio doesn't seem to be working with Linux, waiting for the dev to fix them then I can re-relese the linux version of the translator

If the application doesn't display the japanese character correctly please follow these steps :
        
        1.Open the Control Panel
        2.Click Region and Language
        3.On the Administrative tab, under Language for non-Unicode programs, click "change system locale..."
        4.Set the Current system locale as "Japanese(Japan)"