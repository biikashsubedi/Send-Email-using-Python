import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('.verify_email.html').read_text())

email = EmailMessage()
email['from'] = 'Bikash Subedi'
email['to'] = 'biiikashsubedi@gmail.com'
email['subject'] = 'Creating Email Sender From Python!!'

email.set_content(html.substitute({'firstname': 'Bikash', 'lastname': 'Subedi'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('XXXXX@gmail.com', 'XXXXXXXX')
    smtp.send_message(email)
    print("WOW :), I did this!!")