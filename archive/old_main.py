# import smtplib
# # def send_emails():
#     today = date.today()
#     # Textual month, day and year	
#     today_ = today.strftime("%B %d, %Y")
#     ############################################# USER1 ############################################
#     # connect with Google's servers
#     smtp_ssl_host = 'smtp.gmail.com'
#     smtp_ssl_port = 465
#     # use username or email to log in
#     username = config[env_].user1
#     password = config[env_].pw1
#     name = config[env_].name1
#     ph = config[env_].ph1

#     from_addr = config[env_].user1
#     to_addrs = config[env_].to_addr

#     # the email lib has a lot of templates
#     # for different message formats,
#     # on our case we will use MIMEText
#     # to send only text
    
#     message = MIMEText(f'''
#     Hi, 

#     Reaching out to be added to the Metro Nashville Public Health Department COVID-19 Vaccine standby list.

#     Contact Info:
#     Name: {name}
#     Ph: {ph}

#     Thank you!
#     -{name.split(' ')[0]}
#     ''')
#     message['subject'] = f'MNPD COVID-19 Vaccine Standby List: {name}, {today_}'
#     message['from'] = from_addr
#     message['to'] = ', '.join([to_addrs])

#     # we'll connect using SSL
#     server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
#     # to interact with the server, first we log in
#     # and then we send the message
#     server.login(username, password)
#     try:
#         server.sendmail(from_addr, to_addrs, message.as_string())
#         print(f'''Successfully sent email from {name.split(' ')[0]} at {datetime.now()}''')
#     except Exception as e:
#         print(e)

#     ############################################# USER2 ############################################
#     # time.sleep(5) # seconds
#     # use username or email to log in
#     username = config[env_].user2
#     password = config[env_].pw2
#     name = config[env_].name2
#     ph = config[env_].ph2

#     from_addr = config[env_].user2
#     to_addrs = config[env_].to_addr

#     # the email lib has a lot of templates
#     # for different message formats,
#     # on our case we will use MIMEText
#     # to send only text

#     message = MIMEText(f'''
#     Hello, 

#     Reaching out to be entered into the Metro Nashville Public Health Department COVID-19 Vaccine Standby List!

#     Contact Info:
#     Name: {name}
#     Phone: {ph}

#     Thank you,
#     -{name.split(' ')[0]}
#     ''')
#     message['subject'] = f'MNPD COVID-19 Vaccine Standby List: {name}, {today_}'
#     message['from'] = from_addr
#     message['to'] = ', '.join([to_addrs])

#     # we'll connect using SSL
#     server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
#     # to interact with the server, first we log in
#     # and then we send the message
#     server.login(username, password)
#     try:
#         server.sendmail(from_addr, to_addrs, message.as_string())
#         print(f'''Successfully sent email from {name.split(' ')[0]} at {datetime.now()}''')
#     except Exception as e:
#         print(e)
#     server.quit()
#     return
        
# def sendgrid():
#     message = Mail(
#         from_email=config[env_].user1,
#         to_emails=config[env_].to_addr,
#         subject='Sending with Twilio SendGrid is Fun',
#         html_content='<strong>and easy to do anywhere, even with Python</strong>')
#     try:
#         sg = SendGridAPIClient(config[env_].SENDGRID_API_KEY)
#         response = sg.send(message)
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)
#     except Exception as e:
#         print(e.message)
#     return
# Scheduling Part of Script 

# def background_thread():
#     schedule_thread = threading.Thread(
#         target=schedules)
#     schedule_thread.start()
#     return '{}'

# continues to run on schedule frequency below

# runs at startup

# def schedules():
#     print(f'Starting service at {startupTs} in Env: {env_}')
#     send_emails()
#     schedule.every(config[env_].refresh["frequency"]).minutes.do(send_emails)
#     while True:
#         schedule.run_pending()
#         time.sleep(3600) # checks if any pending jobs every 3600 seconds -> 1 hour
#     return

# End of scheduling part