import smtplib
import ssl
from email.message import EmailMessage

class mail:
    def __init__(self, subject, body) -> None:
        self.subject = subject
        self.body = body
        self.message = EmailMessage()



class mailSender:
    def __init__(self, subject, body, senderMail, senderPassw) -> None:
        self.mail = mail(subject=subject, body=body)
        self.sender = senderMail
        self.password = senderPassw
        self.message = EmailMessage()
####
    def setMessage(self, receiver):
        self.message["From"] = self.sender
        self.message["To"] = receiver
        self.message["Subject"] = self.mail.subject
        self.message.set_content(self.mail.body)
#####
    def sendEmailTo(self, receiverMail):
        self.setMessage(receiverMail)
        context = ssl.create_default_context()
        print("Sending email to", receiverMail)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender, self.password)
            server.sendmail(self.sender, receiverMail, self.message.as_string())
        print("Email sent ... ")
        

            
