import time

from selenium import webdriver
import datetime

driver = webdriver.Chrome()
url = 'https://www.saucedemo.com/'

driver.get(url)

user = driver.find_element('id', 'user-name')
password = driver.find_element('id', 'password')
login = driver.find_element('xpath', '//*[@id="login-button"]')

if user.is_enabled() and password.is_enabled():
    password.send_keys('secret_sauce')
    user.send_keys('standard_user')
    login.click()

backpack = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]')
backpack.click()
t_shirt = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
t_shirt.click()
jacket = driver.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
jacket.click()
basket = driver.find_element('xpath', '//*[@id="shopping_cart_container"]/a')
basket.click()
driver.save_screenshot('shop.png')
checkout = driver.find_element('xpath', '//*[@id="checkout"]')
checkout.click()

input_name = driver.find_element('id', 'first-name')
input_last_name = driver.find_element('id', 'last-name')
input_postal_code = driver.find_element('id', 'postal-code')

if input_name.is_enabled() and input_last_name.is_enabled() and input_postal_code.is_enabled():
    input_name.send_keys('Pavel')
    input_last_name.send_keys('Alekseev')
    input_postal_code.send_keys('123545')

contin = driver.find_element('xpath', '//*[@id="continue"]')
contin.click()

time.sleep(1)

finish = driver.find_element('xpath', '//*[@id="finish"]')
finish.click()

backhome = driver.find_element('xpath', '//*[@id="back-to-products"]')
backhome.click()

open_menu = driver.find_element('xpath', '//*[@id="react-burger-menu-btn"]')
open_menu.click()

logout = driver.find_element('xpath', '//*[@id="logout_sidebar_link"]')

if logout.is_enabled():
    time.sleep(2)
    logout.click()

time.sleep(5)