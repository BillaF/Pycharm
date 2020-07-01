from selenium import  webdriver
from selenium.webdriver.support.ui import Select


import time


driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32 (4)\chromedriver.exe")

driver.maximize_window()

driver.get("https://candidate1:FjfercQ8V*Jq@igstg.com/fundraiser/help-ek-fekf-new")

#driver.find_element_by_xpath("//*[@id='myModal1']/div/div/div/button")

driver.find_element_by_id("cmp-nfr-top-side-donate").click()

driver.find_element_by_id("story-popup-donate-amt-option3").click()

element=driver.find_element_by_id("donate_modal_currency_dropdown")
drop=Select(element)
drop.select_by_visible_text('CAD')

driver.find_element_by_id("full_name").send_keys("Avantika")

driver.find_element_by_id("switch").click()

driver.find_element_by_id("email_receipt").send_keys("avantika.golu12@gmail.com")

time.sleep(5)

ele=driver.find_element_by_id("mobile_country_code")

drop1=Select(ele)
drop1.select_by_index("1")

driver.find_element_by_id("mobile").send_keys("845632100000000")

driver.find_element_by_id("city_text").send_keys('Mumbai')


driver.find_element_by_id("isWhatsAppSubscription").click()

driver.find_element_by_id("story-popup-donate-button").click()

#inputboxes=driver.find_elements_by_class_name("form-control custom-form-control error-form-control-bottom")
#print(len(inputboxes))

driver.switch_to.frame(driver.find_element_by_tag_name('stripeXDM_default231680_provider'))
cc_input=driver.find_element_by_css_selector("cardNumber").send_keys("4242424242424242")









