import requests
from lxml import etree
import smtplib
from email.mime.text import MIMEText

url = "https://www.bilibili.com/v/popular/rank/all"
content = etree.HTML(requests.get(url).text)
temp = content.xpath("//a[@class='title']/text()")

mail_host = 'smtp.126.com'  
mail_user = 'maxnbd'
mail_pass = 'AXUBECLAOYRFPTWG'   
sender = 'maxnbd@126.com'  
receivers = ['2644087688@qq.com']  

b = '_____________________________________________________________________________________formGITHUB\n'.join(temp)

message = MIMEText(b,'plain','utf-8')
message['Subject'] = 'Conduction Of Bili Tops' 
message['To'] = receivers[0]  

f = open("./README.md")

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass) 
    smtpObj.sendmail(sender,receivers,message.as_string()) 
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误
