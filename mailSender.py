import smtplib
import ssl
from email.message import EmailMessage

class mail:
    def __init__(self, subject, body) -> None:
        self.subject = subject
        self.body = body



class mailSender:
    def __init__(self, mail) -> None:
        self.mail = mail
        self.sender = "sender@gmail.com"
        self.password = "gmail_sender_password"
        self.receiver = "receiver@gmail.com"

    def __init__(self, subject, body) -> None:
        self.mail = mail(subject=subject, body=body)
        self.sender = "sender@gmail.com"
        self.password = "gmail_sender_password"
        self.receiver = "receiver@gmail.com"

    def setMessage(self):
        message = EmailMessage()
        message["From"] = self.sender
        message["To"] = self.receiver
        message["Subject"] = self.mail.subject
        message.set_content(self.mail.body)
        return message

    def SendEmail(self):
        context = ssl.create_default_context()
        print("Sending email to", self.receiver)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receiver, self.setMessage().as_string())
        print("Email sent ... ")
            
