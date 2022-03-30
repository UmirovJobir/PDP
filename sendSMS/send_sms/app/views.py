import datetime
from datetime import date

from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth
from .models import Send, User


def send(recipient, message_id, text):
    url = 'http://91.204.239.44/broker-api/send/'
    user = "uzagrosugurta"
    password = "QUz2v79S"
    headers = {'content-type': 'application/json'}
    sms_message = {
        "messages":
            [
                {
                    "recipient": recipient,
                    "message-id": message_id,
                    "sms": {
                        "originator": "3700",
                        "content": {
                            "text": text
                        }
                    }
                }
            ]
    }
    response = requests.post(url=url, auth=HTTPBasicAuth(user, password), headers=headers, json=sms_message)
    # result_list = []
    # result_list.append(sms_message, response.status_code)
    Send.objects.create(
        recipient=recipient,
        message_id=message_id,
        text=text,
        status=response.status_code
    )
    return response.status_code


def check_date(request):
    date_input = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_input.split('-'))
    date_input = datetime.date(year, month, day)
    today = date.today()

    user = User.objects.get(id=1)

    if date_input == today:
        return redirect(send(user.user_number, user.message_id, user.text))
