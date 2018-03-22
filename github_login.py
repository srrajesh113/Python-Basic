from selenium import webdriver
#opening the browser
browser=webdriver.Chrome(executable_path="/home/user/Downloads/chromedriver_linux64/chromedriver.exe")
browser.get('https://github.com/login')
#typing email or username or phone number
user=browser.find_element_by_xpath('//*[@id="login_field"]')
user.send_keys("rajesh.17cs@cmr.edu.in")
#typing the password
password=browser.find_element_by_xpath('//*[@id="password"]')
password.send_keys("rajesh123$")
#login in the fb account
lb=browser.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[3]').click()
