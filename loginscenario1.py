from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class login():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome(executable_path='/Users/QuintonMills/Desktop/SeleniumKitchen/chromedriver')
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        login = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login.click()

        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")

        time.sleep(3)

        emailField.clear()

        time.sleep(3)

        emailField.send_keys("test")



ff = login()
ff.test()