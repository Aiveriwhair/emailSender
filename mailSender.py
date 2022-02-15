import smtplib
import ssl
from email.message import EmailMessage

class mail:
    def __init__(self, subject, body) -> None:
        self.subject = subject
        self.body = body
        self.message = EmailMessage()



class mailSender:
    def __init__(self, subject=None, body=None, senderMail=None, senderPassw=None) -> None:
        self.mail = mail(subject=subject, body=body)
        self.sender = senderMail
        self.password = senderPassw
        self.message = ""
####
    def setMessage(self, receiver=None):
        self.message = EmailMessage()
        self.message["From"] = self.sender
        self.message["To"] = receiver
        self.message["Subject"] = self.mail.subject
        self.message.set_content(self.mail.body)
#####
    def sendEmailTo(self, receiversMail=[]):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender, self.password)
            for receiver in receiversMail:
                print("Sending email to", receiver)
                self.setMessage(receiver)
                server.sendmail(self.sender, receiver, self.message.as_string())
                print("Email sent ... ")
        

            
