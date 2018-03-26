from gpiozero import MotionSensor
import os
import time
pir = MotionSensor(4)
time.sleep(3)
if pir.motion_detected:
    print("Motion Detected")
    os.system("fswebcam -F 5 --fps 30 1280*720 /home/cs2017a207/Desktop/image.jpg")
    print("taken")
else:
    print("No motion")
    
