from datetime import datetime, date
from email.mime.text import MIMEText
import os
import schedule
import smtplib
import threading
import time

from config import *

startupTs = datetime.now()

global env_
env_ = env('_ENV')

def main():
    today = date.today()
    # Textual month, day and year	
    today_ = today.strftime("%B %d, %Y")
    ############################################# USER1 ############################################
    # connect with Google's servers
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    # use username or email to log in
    username = config[env_].user1
    password = config[env_].pw1
    name = config[env_].name1
    ph = config[env_].ph1

    from_addr = config[env_].user1
    to_addrs = config[env_].to_addr

    # the email lib has a lot of templates
    # for different message formats,
    # on our case we will use MIMEText
    # to send only text
    
    message = MIMEText(f'''
    Hi, 

    Reaching out to be added to the Metro Nashville Public Health Department COVID-19 Vaccine standby list.

    Contact Info:
    Name: {name}
    Ph: {ph}

    Thank you!
    -{name.split(' ')[0]}
    ''')
    message['subject'] = f'MNPD COVID-19 Vaccine Standby List: {name}, {today_}'
    message['from'] = from_addr
    message['to'] = ', '.join([to_addrs])

    # we'll connect using SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # to interact with the server, first we log in
    # and then we send the message
    server.login(username, password)
    try:
        server.sendmail(from_addr, to_addrs, message.as_string())
        print(f'''Successfully sent email from {name.split(' ')[0]} at {datetime.now()}''')
    except Exception as e:
        print(e)

    ############################################# USER2 ############################################
    # time.sleep(5) # seconds
    # use username or email to log in
    username = config[env_].user2
    password = config[env_].pw2
    name = config[env_].name2
    ph = config[env_].ph2

    from_addr = config[env_].user2
    to_addrs = config[env_].to_addr

    # the email lib has a lot of templates
    # for different message formats,
    # on our case we will use MIMEText
    # to send only text

    message = MIMEText(f'''
    Hello, 

    Reaching out to be entered into the Metro Nashville Public Health Department COVID-19 Vaccine Standby List!

    Contact Info:
    Name: {name}
    Phone: {ph}

    Thank you,
    -{name.split(' ')[0]}
    ''')
    message['subject'] = f'MNPD COVID-19 Vaccine Standby List: {name}, {today_}'
    message['from'] = from_addr
    message['to'] = ', '.join([to_addrs])

    # we'll connect using SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # to interact with the server, first we log in
    # and then we send the message
    server.login(username, password)
    try:
        server.sendmail(from_addr, to_addrs, message.as_string())
        print(f'''Successfully sent email from {name.split(' ')[0]} at {datetime.now()}''')
    except Exception as e:
        print(e)
    server.quit()
    return
        
# Scheduling Part of Script 

def background_thread():
    schedule_thread = threading.Thread(
        target=schedules)
    schedule_thread.start()
    return '{}'

def schedules():
    while True:
        schedule.run_pending()
        time.sleep(3600) # checks if any pending jobs every 3600 seconds -> 1 hour


# continues to run on schedule frequency below
schedule.every(config[env_].refresh["frequency"]).minutes.do(main)

# End of scheduling part

# runs at startup
print(f'starting service at {startupTs} in env:{env_}')
main()

if __name__ == '__main__':
     try: 
         background_thread()
     except Exception as e:
         print('main() error: ', e)
