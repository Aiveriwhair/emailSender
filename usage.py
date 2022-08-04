from mailSender import mailSender

sender = mailSender(subject="Mail sent with python", 
                    body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce auctor luctus quam.",
                    senderMail="sender@gmail.com",
                    senderPassw="gmailSenderPassword")
sender.sendEmailTo(["receiver1@gmail.com", receiver2@gmail.com])
