from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://192.168.0.122:<NodePort>")
time.sleep(2)
assert "Hello from Flask" in driver.page_source
driver.quit()
