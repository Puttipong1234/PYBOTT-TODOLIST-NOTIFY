import os

spreadsheet_key = os.environ.get('SPREADSHEET_KEY') # setup env variable on heroku
service_account_key_file = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') # setup env variable on heroku
notify_token = os.environ.get('LINE_NOTIFY_TOKEN') # setup env variable on heroku
SPREADSHEET_LINK = os.environ.get('SPREADSHEET_LINK') # setup env variable on heroku

#ADDING BUILDPACK FOR GOOGLE SHEET IN SETTINGS
#https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack
