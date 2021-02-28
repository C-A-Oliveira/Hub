
import os
import smtplib
import imghdr
import json
from email.message import EmailMessage

msg_body = '''
Hello, {fuckwit}

Thank you for get in touch via my shitty web-page :]

This is a automatic message and I'll be repplying directlly soon enough. Maybe in 1 or 2 business days. No need to fill the form again.

Take care, the cake is a lie!!!

Kind regards
- Cesar Augusto "Razek" Oliveira
'''

def send_it(name, email_to, subject ):
    with open(os.environ.get('STUFF_VARS')) as env:
        VARS = json.load(env)
    EMAIL_ADDR = VARS['mail']
    EMAIL_PASS = VARS['pass']

    contacts = ['cesar.razek29@gmail.com', 'test@example.com']

    msg = EmailMessage()
    msg['From']     = EMAIL_ADDR
    msg['Subject']  = subject
    msg['To']       = email_to

    # FUCK THIS PIECE OF CRAP, CAN'T FIND THE FILE MY ASS
    '''msg_body = open("message_body.txt", "r")
    print(msg_body.read().format(name))'''
    msg.set_content(msg_body.format(fuckwit=name))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDR, EMAIL_PASS)
        smtp.send_message(msg)
    
    print(f"> automatic email to {name} @ {email_to} sent.")