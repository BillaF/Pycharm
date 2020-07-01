from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path ="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com")


#driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div[2]/div/form/div[2]/button").click()

user= driver.find_element_by_name("userName")
print(user.is_displayed())  #return true or false based of element status
print(user.is_enabled())

pswd= driver.find_element_by_name("password")

print(user.is_displayed())
print(user.is_enabled())


user.send_keys("mercury")
pswd.send_keys("mercury")

driver.find_element_by_name("login").click()
roundtrip=driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of  round trip radio button", roundtrip.is_selected()) #print status of radio button round trip


onetrip= driver.find_element_by_css_selector("input[value=oneway]")
print("status of oneway trip radio button", onetrip.is_selected())




