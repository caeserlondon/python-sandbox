# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# chrome_driver_path = "/Users/caeseribrahim/Documents/projects/chromedriver-mac-arm64/chromedriver"
#
# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=service)




#Import the necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By

#Initialize the WebDriver
driver = webdriver.Chrome()

#Open page
driver.get("https://www.python.org/")

#Locate the element
# element = driver.find_element(By.CLASS_NAME,"icon_calendar")
# title = driver.find_elements(By.CLASS_NAME, "icon-calendar")
# print(title)

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# docs_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(docs_link.text)
#
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
#
# print(bug_link.get_attribute("href"))
#
# print(bug_link.text)

# driver.close()
driver.quit()