import gspread_db
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import datetime
from config import spreadsheet_key , service_account_key_file , SPREADSHEET_LINK

# You can learn more about how to register your
# service and get API credentials at:
# https://gspread.readthedocs.io/en/latest/oauth2.html

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(service_account_key_file, scope)

client = gspread_db.authorize(credentials)
db = client.open_by_key(spreadsheet_key)

def get_noti_data():

    res = []

    DATA = db["Sheet1"] # name of your todolist sheet


    today = datetime.datetime.now()
    for i in DATA.get_all_records():
        TIME_LEFT = 0
        for k,v in i.items():

            if k == "ISSUE DATE" and v != "":
                format_str = '%d/%m/%Y' # The format
                datetime_obj = datetime.datetime.strptime(v, format_str)
                delta = datetime_obj - today
                TIME_LEFT = delta.days # calculate for time left to done task เหลือเวลาเท่าไหร่
                
            if not v == "":
                pass

        
        if i["ISSUE DATE"] != "":

            i["TIME_LEFT"] = TIME_LEFT
            res.append(i)


    res = sorted(res, key = lambda i: i['TIME_LEFT']) #ทำการเรียงลำดับงานที่ต้องทำให้เสร็จก่อน


    datas = res

    data = [datas[x:x+8] for x in range(0, len(datas),8)] #ทำการส่งข้อความไปทีละ 8 todo list

    result = []

    for number,each in enumerate(data):

        data_to_noti = "📋TODOLIST .... 📋 \n"
        data_to_noti_1_in = False
        data_to_noti_2_in = False

        data_to_noti_1 = "\n🥵ต้องทำเสร็จอีกไม่กี่วัน...\n"
        data_to_noti_2 = "\n😱งานภายในสัปดาห์นี้....\n"

        for i in each:

            try:
                int(float(i["PROGRESS"]))
                
            except:
                continue

            if 0 < int(i["TIME_LEFT"]) <= 3 : 
                if int(i["PROGRESS"]) < 80: #ถ้าเวลาน้อยกว่า 3 วันแล้ว progress ยังไม่ถึง 80%
                    data_to_noti_1_in = True
                    data_to_noti_1 += "\n👉อีก {} วัน ต้องส่ง {}\n🚧ความคืบหน้า{}%  \n🧍ผู้รับผิดชอบ {} รีบหน่อยจร้าาา\n".format(i["TIME_LEFT"],i["TITLE"],i["PROGRESS"],i["OWNER"])
                
                else: 
                    data_to_noti_1_in = True
                    data_to_noti_1 += "\n👉อีก {} วัน ต้องส่ง {}\n🟢ความคืบหน้า{}%  \n🧍ผู้รับผิดชอบ {} เยี่ยมมาก!\n".format(i["TIME_LEFT"],i["TITLE"],i["PROGRESS"],i["OWNER"])
                


        for i in each:
            try:
                int(float(i["PROGRESS"]))
            
            except:
                continue
            if 3 < int(i["TIME_LEFT"]) <= 7:

                if int(float(i["PROGRESS"])) < 30: #ถ้าเวลาน้อยกว่า 7 วันแล้ว progress ยังไม่ถึง 30%
                    data_to_noti_2_in = True
                    data_to_noti_2 += "\n👉อีก {} วัน ต้อง {}\n🚧ความคืบหน้า{}%  \n🧍ผู้รับผิดชอบ {}\n".format(i["TIME_LEFT"],i["TITLE"],i["PROGRESS"],i["OWNER"])
                
                else:
                    data_to_noti_2_in = True
                    data_to_noti_2 += "\n👉อีก {} วัน ต้อง {}\n🟢ความคืบหน้า{}%  \n🧍ผู้รับผิดชอบ {} เยี่ยมมาก!\n".format(i["TIME_LEFT"],i["TITLE"],i["PROGRESS"],i["OWNER"])
        
        if data_to_noti_1_in:
            data_to_noti = data_to_noti + data_to_noti_1
            data_to_noti_1_in = False
            result.append(data_to_noti)

        if data_to_noti_2_in:
            data_to_noti = data_to_noti + data_to_noti_2
            data_to_noti_2_in = False
            result.append(data_to_noti)

    data_to_noti_3 = "\nกรุณาอัพเดต Progress หรืออ่านรายละเอียดงาน ได้ที่ \n{}".format(SPREADSHEET_LINK)

    result.append(data_to_noti_3)
    return result