from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def teste_bug001_sobrenome_esapacos():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        ).click()

        driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        ).click()

        
        driver.find_element(By.ID, "checkout").click()
      
        driver.find_element(
            By.ID,
            "first-name"
        ).send_keys("Miguel")

        driver.find_element(
            By.ID,
            "last-name"
        ).send_keys("   ")  # Apenas espaços

        driver.find_element(
            By.ID,
            "postal-code"
        ).send_keys("70000000")


        driver.find_element(
            By.ID,
            "continue"
        ).click()

        time.sleep(1)

        
        assert "checkout-step-two.html" in driver.current_url, \
            "O sistema bloqueou o checkout."

        print("BUG REPRODUZIDO: sistema aceitou sobrenome contendo apenas espaços.")

    finally:
        driver.quit()
