import datetime
from datetime import date


def send_sms():
    print('Ishladi')


date_input = input('Enter a date in YYYY-MM-DD format: ')
year, month, day = map(int, date_input.split('-'))
date_input = datetime.date(year, month, day)
today = date.today()

if date_input == today:
    send_sms()
print("Date is wrong!")
