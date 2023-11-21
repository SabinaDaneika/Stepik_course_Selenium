from selenium import webdriver
import time

browser = webdriver.Chrome()
time.sleep(5)
browser.execute_script("document.title='Script executing'; alert('Robots at work');")
time.sleep(5)

browser.quit()