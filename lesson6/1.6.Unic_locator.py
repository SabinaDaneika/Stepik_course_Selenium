from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    firstlink = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(firstlink)

    # заполняем поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_class > [placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".second_class > [placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".third_class > [placeholder='Input your email']")
    input3.send_keys("fdsfds@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

finally:
    time.sleep(5)
    browser.quit()