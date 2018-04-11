import RPi.GPIO as GPIO
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

GPIO.setmode(GPIO.BCM)

# init list with pin numbers
c=21

# loop through pins and set mode and state to 'high'
GPIO.setup(c,GPIO.IN)
GPIO.setup(20, GPIO.OUT) 
GPIO.output(20, GPIO.HIGH)

# time to sleep between operations in the main loop
SleepTimeS = 60


def rk():
    os.system("fswebcam -F 5 --fps 30 1280*720 /home/pi/Desktop/image1.jpg")
    print("pic taken")
    
def SendMail(executable_path="/home/pi/Desktop/image1.jpg"):
    img_data = open("/home/pi/Desktop/image1.jpg", 'rb').read()
    msg = MIMEMultipart()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("jaisurya190@gmail.com", "jairose19")
    text = MIMEText("soil detection")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename("/home/pi/Desktop/image1.jpg"))
    msg.attach(image)
    server.sendmail("jaisurya190@gmail.com", "srrajesh113@gmail.com", msg.as_string())
    print("email send")
    
while True:
    v=GPIO.input(c)
        
    if(v == 1): #mud is dry soil moisture sensor will detect and supply water to the plant 
        GPIO.output(20, GPIO.HIGH)#it will check again after 10 seconds
        print("soil is dry")
        rk()
        SendMail()
        time.sleep(SleepTimeS);

    else:       #mud is wet soil moisture sensor will detect and does not supply water to the plant            
        GPIO.output(20, GPIO.LOW)
        print("soil is wet")
        rk()
        SendMail()
        time.sleep(SleepTimeS);
        
        
