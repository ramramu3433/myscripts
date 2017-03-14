import smtplib
import sys
from email.mime.text import MIMEText

smtp_host = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP()
server.connect(smtp_host,smtp_port)
server.ehlo()
server.starttls()
user="ramramu.jr@gmail.com"
password="janakiram@123"

server.login(user,password)

f=open("test")
msg = MIMEText(f.read())

textfile = "test"
msg['Subject']= ' The content is %s ' % textfile
From= 'ramramu.jr@gmail.com'
To= sys.argv[1] 

server.sendmail(From,To,msg.as_string())

server.quit()

