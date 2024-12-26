import smtplib, ssl
import os

def send_email(message):

    host = "smtp.gmail.com"
    port =465

    username = "linbinbin2016@gmail.com"
    password =os.getenv("PASSWORD")
    
    receiver = "linbinbin2016@gmail.com"

    context=ssl.create_default_context()
  
    with smtplib.SMTP_SSL(host, port, context = context) as server:
        print(password)
        server.login(username, password)
       
        server.sendmail(username, receiver, message)