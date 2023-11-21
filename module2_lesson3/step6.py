from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

browser.find_element(By.TAG_NAME, 'button').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element(By.ID, 'input_value')
y = str(math.log(abs(12*math.sin(int(x.text)))))

browser.find_element(By.ID, 'answer').send_keys(y)
browser.find_element(By.CLASS_NAME, 'btn').click()
time.sleep(5)
browser.quit()