from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options=Options()
chrome_options.add_argument("--headless")

user = ["101606005","101603273","101606004"]
pwd = ["4563","1008","12345"]

#driver=webdriver.Chrome()
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://172.31.1.6:8090/httpclient.html")

elem = driver.find_element_by_id("username")
elem.send_keys(user[0])
elem = driver.find_element_by_id("password")
elem.send_keys(pwd[0])
elem.send_keys(Keys.RETURN)

time.sleep(5)

t=driver.find_element_by_id("loginfailed").text
a=t.find('Login failed.')
print(t)
print(a)
if(a==-1):
    print("login successful for "+user[0])
i=1
while(a!=-1 and i<len(user)):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user[i])
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(pwd[i])
    elem.send_keys(Keys.RETURN)
    
    time.sleep(5)
    t=driver.find_element_by_id("loginfailed").text
    a=t.find('Login failed.')
    print(t)
    print(a)
    if(a==-1):
        print("login successful for "+user[i])
    i=i+1
if(a!=-1):
    print("login was not succesfull for any user")

##if(a==-1):
##    time.sleep(5)
##    driver.find_element_by_id("loginbutton").click()
##    print("logout was successful")
##    driver.close()

    
    
    

#<div id="loginfailed" class="red">Login failed.
#Invalid user name/password. Please contact the administrator. </div>
