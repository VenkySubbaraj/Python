import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = "<mail_address>@gmail.com"
    msg['from'] = user
    password = ""
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__" :
    email_alert("Failed_oject", "Please check one file is failed", "mail_address@gmail.com")
