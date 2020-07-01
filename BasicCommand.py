from selenium import webdriver
from selenium.webdriver.common.keys import keys
import  time


#chrome

driver=webdriver.Chrome(executable_path="C:\Users\user\Documents\UiPath\chromedriver_win32\chromedriver.exe")
driver.get("https://www.irctc.co.in/nget/train-search")
print(driver.title)  #return the title of the page
print(driver.current_url)  #return url of the page

driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div[2]/div/form/div[2]/button").click()

time.sleep(5)

driver.close()