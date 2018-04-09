import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
def SendMail(executable_path="/home/rajesh/Pictures/Screenshot from 2018-03-01 15-55-00.png"):
    img_data = open("/home/rajesh/Pictures/Screenshot from 2018-03-01 15-55-00.png", 'rb').read()
    msg = MIMEMultipart()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("srrajesh113@gmail.com", "rajesh123$")
    text = MIMEText("hello")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename("/home/rajesh/Pictures/Screenshot from 2018-03-01 15-55-00.png"))
    msg.attach(image)
    server.sendmail("srrajesh113@gmail.com", "rajesh.17cs@cmr.edu.in", msg.as_string())
SendMail()
        
