from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.google.com")
assert "Google" in driver.title
elem = driver.find_element_by_id('lst-ib')
elem.clear()
elem.send_keys("Python is rad!")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()
