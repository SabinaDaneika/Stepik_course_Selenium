from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

field = browser.find_element(By.ID, 'answer')
field.send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
option1.click()

option2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
option2.click()

button = browser.find_element(By.CLASS_NAME, 'btn-default')
button.click()
time.sleep(9)

browser.quit()
