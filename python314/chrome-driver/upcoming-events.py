#Import the necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By

#Initialize the WebDriver
driver = webdriver.Chrome()

#Open page
driver.get("https://www.python.org/")

events_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(events_times)):
    events[n] = {
        "time": events_times[n].text,
        "name": events_names[n].text,
    }

print(events)


    # event_date = event.get_attribute("datetime")
    # upcoming_event = {'time':event_name, 'name': event_date }
    # events_list.update(upcoming_event)

# print(events_list)