from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.kagrana.com")
assert "Home - Kagrana Software Pvt. Ltd. | Kagrana Software Pvt. Ltd." in driver.title
elem = driver.find_element_by_name("s")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "Nothing Found" in driver.page_source
driver.close()