**ลิ้งดาวโหลดอยู่ด้านขวาตรง "Releases" ไม่ใช่ปุ่มด้านบน หรือจะโหลดจากลิ้งด้านล่างก็ได้**

https://github.com/Gusb3ll/Holotranslator/releases/tag/v1.0

# วิธีการใช้งาน #

1. ดาวโหลดไฟล์ซิปใน Releases ด้านขวาและรัน "v1.exe" หลังจากแตกไฟล์ออกมา

2. เมื่อเปิดโปรแกรมขึ้นมาจะโดนถามว่า "Do you want to list your SteroMix index id?" ให้ตอบ "yes" ไป

3. ให้ใส่เลขตัวเลขที่โผล่ขึ้นมาใน list ตัวแรกเมื่อโปรแกรมถาม "Your device index id"

4. Audio Channel ส่วนตรงนี้ให้เว้นว่างไปได้เลยเพราะตัว StereoMix จะมีแค่ 2 Channels

5. Time between each translation ให้เว้นว่างไป หรือจะใส่เวลาตามต้องการได้ (แนะนำให้ใส่มากกว่า 10 วิเพราะจะได้ครบประโยค)

6. เปิดคลิปอะไรก็ได้ที่มีคนพูดภาษาญี่ปุ่น(คลิปเพลงใช้ไม่ได้เพราะว่ามีเสียงรบกวนมากเกินไป)

ปล. ตัวโปรแกรมจะแปลเป็นภาษาอังกฤษสำหรับตอนนี้เท่านั้น อัปเดตหน้าจะเพิ่ม Support ภาษาไทยมาให้

ปล2. อย่าคาดหวังว่าคำที่ได้จะตรงเปะกับคำที่พูดทุกคำเพราะเป็นการตรวจจับเสียงและนำไปแปลอีกทีนึงทำให้มีความแม่นยำที่ต่ำ

# วิธีแก้ภาษาญี่ปุ่นไม่ขึ้นในตัวโปรแกรม #

1. เปิด "แผนควบคุม"

2. เข้าไปตรง "ภาษาและภูมิภาค"

3. ในหัวข้อ "Administrative" ใต้หัวข้อ "Language for non-Unicode programs" กด "change system locale"

4. เปลี่ยนเป็น "Japanese" จากนั้นคอมพิวเตอร์จะทำการ restart

## วิดีโอแสดงการใช้งาน

https://www.youtube.com/watch?v=25mmeiiQOGU

## วิธีแก้ StereoMix ใช้ไม่ได้

https://www.youtube.com/watch?v=MIb1PHfHtUw

## วิธีย้าย Region ไปเป็นญี่ปุ่นสำหรับคนที่ภาษาญี่ปุ่นไม่ขึ้น

https://www.youtube.com/watch?v=Ll8fbEGuIKU

ติดต่อได้ที่ Discord : Gusbell l.#3973

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Usage :
        
1. Download the release and run "v1.exe" and type "yes" into the console to display your StereoMix index id (Recommend for first time user), or "all" if you want to list all device and it's index id
        
3. Input your first StereoMix index id into the console when asked to
        
4. Adjust the channels of your input device (StereoMix default is 2)
        
5. Adjust the time between each translation and you're good to go!

Note : If your "StereoMix" doesn't pick up any sound, try to set the default device to SteroMix and its output to your headphone, then plug your headphone jack into it

If the application doesn't display the japanese character correctly please follow these steps :
        
1. Open the Control Panel
        
2. Click Region and Language
        
3. On the Administrative tab, under Language for non-Unicode programs, click "change system locale..."
        
4. Set the Current system locale as "Japanese(Japan)"

Compiling :

1. Clone this repo

2. Create Python environment and install enverything in "requirements.txt" (For py audio, install it with included wheel)

3. Install PyInstaller

4. Navigate to root directory and type "pyinstaller --onefile --icon=kanata.ico ./main.py"

5. your .exe file should be in "dist" folder that PyInstaller create

Contact Discord : Gusbell l.#3973
