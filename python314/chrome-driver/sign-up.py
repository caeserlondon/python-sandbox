from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://secure-retreat-92358.herokuapp.com/")
#
# first_name = wait.until(
#     EC.visibility_of_element_located((By.NAME, "fname"))
# )
# first_name.send_keys("Caeser")
# first_name.send_keys(Keys.ENTER)
#
# last_name = wait.until(
#     EC.visibility_of_element_located((By.NAME, "lname"))
# )
# last_name.send_keys("Ibrahim")
# last_name.send_keys(Keys.ENTER)
#
# email = wait.until(
#     EC.visibility_of_element_located((By.NAME, "email"))
# )
# email.send_keys("caeser@gmail.com")
# email.send_keys(Keys.ENTER)

first_name = driver.find_element(By.CLASS_NAME, "top")
last_name = driver.find_element(By.CLASS_NAME, "middle")
email = driver.find_element(By.CLASS_NAME, "bottom")
button = driver.find_element(By.CLASS_NAME, "btn")

first_name.send_keys("Caeser")
first_name.send_keys(Keys.ENTER)
last_name.send_keys("Ibrahim")
last_name.send_keys(Keys.ENTER)
email.send_keys("caeser@gmail.com")
email.send_keys(Keys.ENTER)



button.click()