import smtplib

account = "#アカウント名" 
password = "#パスワード" 

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(account, password)
