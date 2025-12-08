from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/caeseribrahim/Documents/projects/chromedriver-mac-arm64/chromedriver"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://amazon.com")

# driver.close()
driver.quit()