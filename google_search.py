import speech_recognition as sr
from selenium import webdriver
import time

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')
 
try:
    text = r.recognize_google(audio)
    print('Google thinks you said:\n' + text)
    time.sleep(3)
    browser=webdriver.Chrome(executable_path="/home/rajesh/Downloads/chromedriver_linux64 (1)/chromedriver.exe")
    browser.get("https://www.google.co.in/search?q")
    user=browser.find_element_by_xpath('//*[@id="lst-ib"]')
    user.send_keys(text)
    user=browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()
 
except Exception as e:
    print (e)
    
