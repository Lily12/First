# loginOpms
# 2021/2/26
# create by grace hu

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# 隐式等待
driver.implicitly_wait(10)
#访问网址
driver.get('http://192.168.1.44:8088/')
#登陆输入登陆名密码,点击登陆
driver.find_element_by_name('username').send_keys('libai')
driver.find_element_by_name('password').send_keys('opmsopms123')
# driver.find_element_by_tag_name('button').click()
driver.find_element_by_css_selector('#login-form > div.login-wrap > button').click()
# webElementWait(driver, 10, 0.5, By.CSS_SELECTOR, '.fa-plane').click()


