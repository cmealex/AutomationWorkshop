# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# prof = webdriver.FirefoxProfile()
# prof.set_preference("browser.startup.homepage_override.mston‌​e", "ignore")
# prof.set_preference("startup.homepage_welcome_url.additional‌​", "about:blank")
# driver = webdriver.Firefox(prof)
driver = webdriver.Firefox()
driver.get("http://www.google.com")
driver.maximize_window()
print driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("cheese!")
elem.submit()
print driver.title
try:
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    print driver.title

finally:
    driver.quit()
