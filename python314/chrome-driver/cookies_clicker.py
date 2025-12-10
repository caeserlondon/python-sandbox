from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

for i in range(10000):
    cookie.click()