from datetime import datetime, date
# from email.mime.text import MIMEText
from flask import Flask
import os
import schedule

import time
# import threading
from mailjet_rest import Client
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

from config import *

startupTs = datetime.now()

global env_
env_ = env('_ENV')
# env_ = 'prod'
app = Flask(__name__)


def mailjet():
    today = date.today()
    # Textual month, day and year	
    today_ = today.strftime("%B %d, %Y")
    api_key = config[env_].MAILJET_KEY
    api_secret = config[env_].MAILJET_SECRET
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": f"{config[env_].user1}",
            "Name": f"{config[env_].name1.split(' ')[0]}"
        },
        "To": [
            {
            "Email": f"{config[env_].user1}",
            "Name": f"{config[env_].name1.split(' ')[0]}"
            }
        ],
        "Subject": f'MNPD COVID-19 Vaccine Standby List: {config[env_].name1}, {today_}',
        "TextPart": "My first Mailjet email",
        "HTMLPart": f'''
Hello, 

Reaching out to be entered into the Metro Nashville Public Health Department COVID-19 Vaccine Standby List!

Contact Info:
Name: {config[env_].name1}
Phone: {config[env_].ph1}

Thank you,
-{config[env_].name1.split(' ')[0]}
''',
        "CustomID": ""
        }
    ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
    return



def test():
    mailjet()
    return


if __name__ == '__main__':
     try: 
         app.run(test()) 
     except Exception as e:
         print('app kickoff error: ', e)
