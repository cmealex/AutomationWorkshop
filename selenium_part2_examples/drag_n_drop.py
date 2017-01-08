# coding=utf-8
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome() # for now problem with FF
driver.get("http://www.w3schools.com/html/tryit.asp?filename=tryhtml5_draganddrop")
driver.maximize_window()
time.sleep(3)
driver.switch_to.frame("iframeResult")

# try:
#
#     element = driver.find_element_by_xpath("//img[@src='img_logo.gif']")
#     target = driver.find_element_by_xpath("//div[@ondrop='drop(event)']")
#     ActionChains(driver).click_and_hold(element).perform()
#     actions = ActionChains(driver)
#     actions.move_to_element(element)
#     # actions.context_click(element)
#     actions.click_and_hold(element)
#     actions.move_to_element(target)
#     actions.release(element)
#     actions.perform()
#     time.sleep(4)
# finally:
#     driver.quit()


driver.get("http://marcojakob.github.io/dart-dnd/basic/web/")
driver.maximize_window()
time.sleep(3)
# driver.switch_to.frame("iframeResult")

try:

    element = driver.find_element_by_xpath("//html/body/div/img[1]")
    target = driver.find_element_by_xpath("//div[@class='trash']")
    ActionChains(driver).drag_and_drop(element, target).perform()
    time.sleep(4)
finally:
    driver.quit()
