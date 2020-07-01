from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.ui import WebDriverWait
import  time


driver =webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32 (4)\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.expedia.com/")
driver.find_element_by_id("tab-flight-tab-hp").click() #filght button



driver.find_element_by_id("flight-origin-hp-flight").send_keys("DEL") #origin
time.sleep(2)
driver.find_element_by_id("flight-destination-hp-flight").send_keys("BOM") #destination
driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("10/6/2020")

driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("18/7/2020")
driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()


#wait=WebDriverWait(driver,10)
#element=wait.until(EC.element_to_be_clickable(driver.find_elements_by_xpath("//*[@id= 'stopFilter_stops-0' ]")))
#element.click()

time.sleep(3)
driver.quit()