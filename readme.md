## Source Code Pybott ทำ TODO List notify ภายในไม่กี่ขั้นตอน

![ScreenShot](https://scontent.fbkk22-2.fna.fbcdn.net/v/t1.0-9/118233601_647323549491993_4702889884263288407_n.png?_nc_cat=106&_nc_sid=19369f&_nc_ohc=5ofwRkRQ-BkAX8cVUAa&_nc_ht=scontent.fbkk22-2.fna&oh=f9f8974bc86fadad933de603079f5d9e&oe=5F6BF6CC)

## วิธีการใช้งานเบื้องต้น
1. cmd > git clone https://github.com/Puttipong1234/PYBOTT-TODOLIST-NOTIFY
2. สร้าง virtual env 
```
python -m venv venv (use python 3.6.8 - 3.6.10)
```
3. activate virtual evironment 
```
(window : venv\Scripts\activate / mac : source venv\bin\activate)
```
3. pip install -r requirements.txt
4. สร้าง Google sheet ของท่าน ตามตัวอย่างดังนี้ https://docs.google.com/spreadsheets/d/1lazyX90x7dRpIV84QhKxKZH0QFN2J-x0P9N_hh1e3hA/edit?usp=sharing โดยให้ header ตรงตามหัวข้อ (อย่าลืม Freeze header ไว้ด้วยนะ ให้มันอยู่แถวที่ 1 ตลอด)

5. เก็บ Spreadsheet_key ของท่านไว้ ดังภาพ
![ScreenShot](https://finnbarsmithdotcom.files.wordpress.com/2014/08/spreadsheet-key.png)

6. เปิดการใช้งาน API ของ Google sheet เข้าไปที่ google cloud console (ไม่สอนแล้วเด้ออ.. ดูโพสเก่าเอานะ หรือ หา Resource การเปิดใช้งาน google sheet api ได้ง่ายๆตาม google เลย)
 - ![ScreenShot](https://raw.githubusercontent.com/Puttipong1234/PYBOTT-TODOLIST-NOTIFY/master/PIC/gcp_api.PNG)
 - ตย. Service Account ![ScreenShot](https://raw.githubusercontent.com/Puttipong1234/PYBOTT-TODOLIST-NOTIFY/master/PIC/service%20account.PNG)
 
 - เก็บไฟล์ credentails.json ไว้นะครับ เราจะนำเนื้อหาในไฟล์ไปใส่ไว้ใน env variable ของขั้นตอนที่ 9

7. เปิดการใช้งาน Line Notification (ไม่สอนแล้วเด้ออ.. หา Resource ได้ง่ายๆตาม google เลย)
    - ![ScreenShot](https://raw.githubusercontent.com/Puttipong1234/PYBOTT-TODOLIST-NOTIFY/master/PIC/line.PNG)
    - สร้างกลุ่ม แล้วแอดเจ้า notify เข้าไป ผ่าน browser จากนั้น เก็บ Token ของกลุ่มเอาไว้นะครับ

8. เรียบร้อย deploy to heroku (install git scm & heroku cli ก่อนเนอะ) เสจแล้วพิมพ์ใน command line ของโปรเจคได้เลยจร้า
    ```
    heroku create

    #จะได้ git repo ของ heroku มา copy ไว้แล้วพิมพ์ต่อเลยยย

    git init
    git add .
    git commit -m "first commit"
    git remote add heroku <ใส่ชื่อ repo heroku ได้เลย>

    heroku ps:scale clock=1
    ```

9. ไปที่หน้า console ของ app-heroku ที่เราได้สร้างไว้แล้วไปที่ settings
    จากนั้นเพิ่ม environment variable ลงไปดังนี้ (เอาตามของที่ตนเองเก็บไว้นะครับ... ยกเว้นตัวแปรบนสุดจะให้ตั้งเป็น google-credentials.json)
    - ![ScreenShot](https://raw.githubusercontent.com/Puttipong1234/PYBOTT-TODOLIST-NOTIFY/master/PIC/heroku.PNG)

    - spread sheet link คือ ลิงค์ที่กดแล้วจะเข้าไปที่หน้า sheet ของเรานะครับ 

    - add buildpack ดังนี้ https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack

10. deploy โล้ด เสร็จแบล้วววว!!
    ```
    git push heroku master
    ```
    อย่าลืม commend ฟังชั่นที่ทดสอบทุกๆ30 วินาทีออกด้วยนะจะ
### notes: หากเกิดข้อผิดพลาดทดลองคำสั่ง

    ```
    heroku logs --tail
    ```

    เพื่อดูว่าเกิดอะไรขึ้นเนอะ หรือจะไปที่ console ของ heroku ก็ได้เช่นกัน
    โดยไปที่ more > View logs

- ![ScreenShot](https://raw.githubusercontent.com/Puttipong1234/PYBOTT-TODOLIST-NOTIFY/master/PIC/heroku.PNG)






#### ฝากติดตาม กดไลค์ กดแชร์ คอนเทน เพื่อเป็นกำลังใจแก่ทีมงานด้วยนะครับขอบพระคุณอย่างสูง