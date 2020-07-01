from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32 (4)\chromedriver.exe")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.switch_to.frame("packageListFrame") #frame1
driver.find_element_by_link_text("com.thoughtworks.selenium").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame") #secondframe
driver.find_element_by_link_text("SeleneseTestCase").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()




