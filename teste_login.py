from selenium import webdriver
from selenium.webdriver.common.by import By

Navegador = webdriver.Chrome()

Navegador.get("https://www.saucedemo.com")

Navegador.find_element(By.ID,"user-name").send_keys("standard_user")
Navegador.find_element(By.ID,"password").send_keys("secret_sauce")
Navegador.find_element(By.ID,"login-button").click()

assert "inventory" in Navegador.current_url

Navegador.quit()
