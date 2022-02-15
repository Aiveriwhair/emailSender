from mailSender import mailSender

sender = mailSender("Mail sent with python", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce auctor luctus quam.",
                    "sender@gmail.com",
                    "gmailSenderPassword")
sender.sendEmailTo(["receiver@gmail.com"])
