from selenium import webdriver
import time
#opening the browser
browser=webdriver.Chrome(executable_path="/home/user/Downloads/chromedriver_linux64/chromedriver.exe")
browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
#typing email or username or phone number
user=browser.find_element_by_xpath('//*[@id="identifierId"]')
user.send_keys("srrajesh113@gmail.com")

#login in the fb account
lb=browser.find_element_by_xpath('//*[@id="identifierNext"]/content').click()
time.sleep(5)
#typing the password
password=browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys("rajesh123$")
#login in the fb account
lb=browser.find_element_by_xpath('//*[@id="passwordNext"]/content').click()

