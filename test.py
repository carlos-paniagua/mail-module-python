import smtplib

account = "turing.test50@gmail.com" #アカウント名
password = "turing53" #パスワード

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(account, password)