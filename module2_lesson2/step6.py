from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")

x = browser.find_element(By.ID, 'input_value')
y = str(math.log(abs(12*math.sin(int(x.text)))))

field = browser.find_element(By.ID, 'answer')
field.send_keys(y)

option1 = browser.find_element(By.ID, 'robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)

option1.click()

option2 = browser.find_element(By.ID, 'robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button = browser.find_element(By.CLASS_NAME, 'btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(5)
browser.quit()


