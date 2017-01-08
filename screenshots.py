# coding=utf-8
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
driver.maximize_window()
time.sleep(3)
driver.switch_to.frame("iframeResult")

try:

    elem = driver.find_element_by_xpath("//button[@onclick='myFunction()']")
    elem.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    driver.switch_to_default_content()
    driver.get_screenshot_as_file("SS.png")
    # alert.dismiss()
    # alert.send_keys(Keys.ENTER)
    # alert.accept()
    time.sleep(2)
finally:
    driver.quit()

