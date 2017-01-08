# coding=utf-8
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()


# Go to the correct domain
driver.get("http://www.example.com")
driver.maximize_window()

# Now set the cookie. Here's one for the entire domain
# the cookie name here is 'key' and its value is 'value'
driver.add_cookie({'name':'key', 'value':'value', 'path':'/'})
# additional keys that can be passed in are:
# 'domain' -> String,
# 'secure' -> Boolean,
# 'expiry' -> Milliseconds since the Epoch it should expire.

# And now output all the available cookies for the current URL
for cookie in driver.get_cookies():
    print cookie
    print "%s -> %s" % (cookie['name'], cookie['value'])

# You can delete cookies in 2 ways
# By name
driver.delete_cookie("CookieName")
# Or all of them
driver.delete_all_cookies()
driver.quit()
