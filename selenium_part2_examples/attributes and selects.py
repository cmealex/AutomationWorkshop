# coding=utf-8
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
driver.maximize_window()
time.sleep(3)
driver.switch_to.frame("iframeResult")

# try:
#
#     # elem = driver.find_element_by_xpath("//html/body/select")
#     select = driver.find_element_by_tag_name("select")
#     allOptions = select.find_elements_by_tag_name("option")
#     for option in allOptions:
#         print "Value is: " + option.get_attribute("value")
#         option.click()
#         time.sleep(2)
#
# finally:
#     driver.quit()

# try:
#     from selenium.webdriver.support.ui import Select
#     select = Select(driver.find_element_by_tag_name("select"))
#     select.select_by_visible_text("Audi")
#     time.sleep(2)
# finally:
#     driver.quit()