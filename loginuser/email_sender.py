import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .email_settings import *

def send_confirmation_email(receiver, confirmation_code):
    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL_ADDRESS
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = receiver.email
    
    html = EMAIL_MESSAGE
    msg.attach(MIMEText(html.format(receiver.username, confirmation_code), 'html'))
    
    sender = EMAIL_ADDRESS
    passwd = EMAIL_PASSWORD
    server = smtplib.SMTP(EMAIL_SMTP, EMAIL_SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.login(sender, passwd)
    try:
        server.sendmail(sender, receiver.email, msg.as_string())
    except:
        print('Error sending mail')
    server.quit()