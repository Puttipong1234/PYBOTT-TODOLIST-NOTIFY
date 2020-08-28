from apscheduler.schedulers.blocking import BlockingScheduler
from config import *
import requests
from noti import get_noti_data

url = 'https://notify-api.line.me/api/notify'
token = notify_token
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

sched = BlockingScheduler()

from datetime import datetime

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=3) # เตือนทุกสิบโมง จันถึงศุกร์ (heroku server +7 GMT thailand)
def notify_app():
    
    data_to_noti = "📋 TODOLIST .... ประจำวันที่ {} 📋".format(str(datetime.now())[:10])
    r = requests.post(url, headers=headers , data = {'message':data_to_noti})
    
    msgs = get_noti_data()
    for msg in msgs:
        r = requests.post(url, headers=headers , data = {'message':msg})
    
    break_line = "📋 Thank For Your Kind Attention ! 📋"
    r = requests.post(url, headers=headers , data = {'message':break_line})

@sched.scheduled_job('interval', seconds=30)
def TEST_CRON_NOTIFY():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    
    data_to_noti = "📋 TODOLIST .... ประจำวันที่ {} 📋".format(str(datetime.datetime.now())[:10])
    r = requests.post(url, headers=headers , data = {'message':data_to_noti})
    
    msgs = get_noti_data()
    for msg in msgs:
        r = requests.post(url, headers=headers , data = {'message':msg})
    
    break_line = "📋 Thank For Your Kind Attention ! 📋"
    r = requests.post(url, headers=headers , data = {'message':break_line})

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()