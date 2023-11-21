from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

browser.find_element(By.CLASS_NAME, 'btn').click()
browser.switch_to.alert.accept()

x = browser.find_element(By.ID, 'input_value')
y = str(math.log(abs(12*math.sin(int(x.text)))))

browser.find_element(By.ID, 'answer').send_keys(y)
browser.find_element(By.CLASS_NAME, 'btn').click()
time.sleep(5)
browser.quit()