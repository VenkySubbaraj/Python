# Python 3.8.0
import smtplib
import time
import imaplib
import email
import traceback 
from imapclient import IMAPClient
# -------------------------------------------------
# Utility to read email from Gmail Using Python
# ------------------------------------------------
ORG_EMAIL = "@gmail.com" 
FROM_EMAIL = "mail_name" + ORG_EMAIL 
FROM_PWD = "" 
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993
mail = IMAPClient('imap.gmail.com', ssl=True, port=993)
mail.login(FROM_EMAIL, FROM_PWD)
totalMail = mail.select_folder('Inbox')
#Shows how many messages are there - both read and unread
print('You have total %d messages in your folder' % totalMail[b'EXISTS'])
delMsg = mail.search(('UNSEEN'))
mail.delete_messages(delMsg)
#Shows number of unread messages that have been deleted now
print('%d unread messages in your folder have been deleted' % len(delMsg))
mail.logout()
