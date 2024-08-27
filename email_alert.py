import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    #msg['from'] = "ithelpdesk@grocerybazaar.store"

    user = "ithelpdesk@grocerybazaar.store"
    msg['from'] = user
    password = "Gbserver@12345"


    server = smtplib.SMTP("mail.grocerybazaar.store", 995)
    server.starttls()
    server.login(user, password)

    server.quit()

    if __name__ == '__main__':
        email_alert("Sample Mail", "Checking for python mail", "samuel.victor@grocerybazaar.store")

