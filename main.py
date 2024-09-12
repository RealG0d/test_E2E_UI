import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()

username = os.getenv('username')
password = os.getenv('password')

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Авторизация на сайте с логином и паролем из файла.env
elem_login = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
elem_login.clear()
elem_login.send_keys(username)
elem_password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
elem_password.clear()
elem_password.send_keys(password)
elem_password.send_keys(Keys.RETURN)

# Добавление товара в корзину и переход к оформлению заказа
elem_buy = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
elem_buy.click()
elem_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
elem_cart.click()
elem_check = driver.find_element(By.ID, "checkout")
elem_check.click()

# Заполнение данных о заказчике
elem_first_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
elem_first_name.clear()
elem_first_name.send_keys('Имя')
elem_last_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']")
elem_last_name.clear()
elem_last_name.send_keys('Фамилия')
elem_adres = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Zip/Postal Code']")
elem_adres.clear()
elem_adres.send_keys('Адрес')
elem_finish = driver.find_element(By.ID, "continue")
elem_finish.click()
elem_finish = driver.find_element(By.ID, "finish")
elem_finish.click()

# Проверка заказа
complete_buy = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "checkout_complete_container"))
)

print('Успешно')

driver.close()
