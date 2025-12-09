from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get("https://www.wikipedia.org/")

english_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#js-link-box-en small"))
)

english_button.click()

search_bar = wait.until(
    EC.visibility_of_element_located((By.NAME,"search"))
)

search_bar.send_keys("Python (programming language)")
search_bar.send_keys(Keys.ENTER)

paragraph = wait.until(
    EC.presence_of_element_located((By.NAME,"paragraph"))
)
print(paragraph.text)

driver.quit()

