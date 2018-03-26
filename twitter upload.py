import tweepy
import os
import time

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)
cfg = { 
"consumer_key"        : "tZjbw3pQHq7RSoWIydmdsMGF7",
"consumer_secret"     : "6Wk5bckQdzHjBrMiS9zP45WIuyASu3GWRr8uwt0BIyTN6kIpeb",
"access_token"        : "3229002192-pzwnGBOin2cpBI0AAusLEyzkVURqd6O78NeMGMz",
"access_token_secret" : "ufBdxnSXfnWyJyEdDk9ljQ3ZtS7xGT1bR2VOfn7iQr4Lx" 
}

api = get_api(cfg)
a=0
b=1
while a<=2:
    img="/home/pi/Desktop/img"+str(b)+".jpg"
    cmd="fswebcam -f 3 --fps 20 -r 800x600"+img
    os.system(cmd)
    print("pic taken")
    api.update_with_media(img,ststus="nice one")
    print("wait")
    time.sleep(5)
    a+=1
    b+=1
    print("success")
