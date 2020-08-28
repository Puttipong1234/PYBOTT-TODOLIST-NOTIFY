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

6. เปิดการใช้งาน API ของ Google sheet เข้าไปที่ google cloud console (ไม่สอนแล้วเด้ออ.. ดูโพสเก่าเอานะ)
 - สร้าง Project ![ScreenShot](https://miro.medium.com/max/770/1*IhH3ZR7EuHcUM6JGXLEQJA.png)


#### ฝากติดตาม กดไลค์ กดแชร์ คอนเทน เพื่อเป็นกำลังใจแก่ทีมงานด้วยนะครับขอบพระคุณอย่างสูง