from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):

        def test_registration1(self):
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element(By.XPATH, "//label[text()='First name*']//following-sibling::input")
            first_name.send_keys("Sabina")
            last_name = browser.find_element(By.XPATH, "//label[text()='Last name*']//following-sibling::input")
            last_name.send_keys("Daneiko")
            email = browser.find_element(By.XPATH, "//label[text()='Email*']//following-sibling::input")
            email.send_keys("example@gmail.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                             "The text of message is wrong")
        def test_registration2(self):
            link = " http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element(By.XPATH, "//label[text()='First name*']//following-sibling::input")
            first_name.send_keys("Sabina")
            last_name = browser.find_element(By.XPATH, "//label[text()='Last name*']//following-sibling::input")
            last_name.send_keys("Daneiko")
            email = browser.find_element(By.XPATH, "//label[text()='Email*']//following-sibling::input")
            email.send_keys("example@gmail.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                             "The text of message is wrong")

            browser.quit()


if __name__ == "__main__":
    unittest.main()

