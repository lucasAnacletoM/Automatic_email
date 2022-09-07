import smtplib
from email.message import EmailMessage
import authenticate
import time
import os
from dotenv import load_dotenv

load_dotenv()

values, spreadsheet_width = authenticate.authenticate_with_google()
old_spreadsheet_width = authenticate.check_sheet_size(values)


your_email = os.environ['email']
your_password = os.environ['password']


def send_email():

    email_body = f"""
        <p>Hi {values[spreadsheet_width-1][1]},</p>
        <p></p>
        <p>We have received your application!</p>
        <p></p>
        <p>Any questions, send me a message.</p>
        <p></p>
        <p>Att. Lucas Anacleto</p>
        """

    msg = EmailMessage()
    msg['Subject'] = "Test of automatich email!"
    msg['From'] = your_email
    msg['To'] = values[spreadsheet_width-1][2]
    password = your_password
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email sent!')


while True:

    if spreadsheet_width != old_spreadsheet_width:

        old_spreadsheet_width = spreadsheet_width
        send_email()

    values, spreadsheet_width = authenticate.authenticate_with_google()

    # this print is to show if the program is running.
    print(f"Analyzing changes {old_spreadsheet_width}")

    time.sleep(3)
