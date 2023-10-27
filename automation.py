from selenium import webdriver
from selenium.webdriver.common.by import By
import pyscreenshot as ImageGrab
import time

driver = webdriver.Firefox(executable_path = "D:\geckodriver/geckodriver")
driver.maximize_window()
driver.get("https://www.psegameshop.com/")

time.sleep(5)

login = driver.find_element(by=By.CLASS_NAME, value="icon-user").click()
time.sleep(10)

m = ImageGrab.grab()
m.save('D:\My Data\DOT Indonesia/screenshot/dot_indonesia.png', 'PNG')
# m.show()

username = driver.find_element(by=By.NAME, value="username")
username.send_keys("ryannuradli")

m = ImageGrab.grab()
m.save('D:\My Data\DOT Indonesia/screenshot/dot_indonesia_username.png', 'PNG')
# m.show()
time.sleep(7)

password = driver.find_element(by=By.NAME, value="password")
password.send_keys("Ryan123456")

m = ImageGrab.grab()
m.save('D:\My Data\DOT Indonesia/screenshot/dot_indonesia_password.png', 'PNG')
# m.show()
time.sleep(7)

remember_me = driver.find_element(by=By.NAME, value="rememberme").click()

m = ImageGrab.grab()
m.save('D:\My Data\DOT Indonesia/screenshot/dot_indonesia_tick.png', 'PNG')
# m.show()
time.sleep(5)

login_button = driver.find_element(by=By.NAME, value="login").click()

m = ImageGrab.grab()
m.save('D:\My Data\DOT Indonesia/screenshot/dot_indonesia_final.png', 'PNG')
# m.show()

time.sleep(5)
driver.close()