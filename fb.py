from selenium import webdriver
#opening the browser
browser=webdriver.Chrome(executable_path="/home/user/Downloads/chromedriver_linux64/chromedriver.exe")
browser.get('https://facebook.com/login/')
#typing email or username or phone number
user=browser.find_element_by_xpath('//*[@id="email"]')
user.send_keys("srrajesh113@gmail.com")
#typing the password
password=browser.find_element_by_xpath('//*[@id="pass"]')
password.send_keys("")
#login in the fb account
lb=browser.find_element_by_xpath('//*[@id="loginbutton"]').click()

