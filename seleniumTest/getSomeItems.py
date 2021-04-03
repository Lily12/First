# getSomeItems
# 2021/3/2
# create by grace hu

from selenium import webdriver
import time
from random import randint
# 创建浏览器驱动
driver = webdriver.Chrome(r'/usr/local/bin/chromedriver')
# 隐式等待
driver.implicitly_wait(10)
#访问网址
driver.get('http://192.168.1.42:8088/')
driver.maximize_window()
#登陆输入登陆名密码,点击登陆
driver.find_element_by_name('username').send_keys('libai')
driver.find_element_by_name('password').send_keys('opmsopms123')
# driver.find_element_by_tag_name('button').click()
driver.find_element_by_css_selector('#login-form > div.login-wrap > button').click()
#点击审批管理
driver.find_element_by_xpath('//ul[@class="nav nav-pills nav-stacked custom-nav js-left-nav"]/li[4]').click()
#点击物品
driver.find_element_by_xpath('//a[@href="/oagood/manage"]').click()
time.sleep(2)
#点击我要领用
driver.find_element_by_css_selector('div.pull-right > a.btn.btn-success').click()
time.sleep(2)
#领取页面
driver.find_element_by_name('purpose').send_keys('办公用品')
driver.find_element_by_name('names[]').send_keys('笔记本')
driver.find_element_by_name('quantitys[]').send_keys(1)
# driver.find_element_by_css_selector('#oagood-form > div:nth-child(2) > div:nth-child(2) > div > input').send_keys('笔记本')
# driver.find_element_by_css_selector('#oagood-form > div:nth-child(2) > div:nth-child(3) > div > input').send_keys('1')
driver.find_element_by_css_selector('a.js-oagoodBoxAdd').click()
time.sleep(1)
driver.find_element_by_css_selector('.js-oagoodBox +div[class="js-oagoodBox"] input[name="names[]"]').send_keys('签字笔')
driver.find_element_by_css_selector('.js-oagoodBox +div[class="js-oagoodBox"] input[name="quantitys[]"]').send_keys('1')
driver.execute_script('window.scrollBy(0, 1000);')
driver.find_element_by_name('content').send_keys('工作使用')
driver.find_element_by_css_selector('.addAvatar > i').click()
# time.sleep(2)
shlist = driver.find_elements_by_xpath('//div[@class="modal-body"]/ul/li')
num = randint(0, len(shlist)-1)
# print(num)
shlist[num].click()
# time.sleep(1)
driver.find_element_by_xpath('//button[@type="submit"]').click()
# print(driver.find_elements_by_link_text(' 操作'))
driver.find_elements_by_xpath('//button[@class="btn btn-primary dropdown-toggle"]')[0].click()
driver.find_elements_by_css_selector('a.js-oagood-status')[0].click()

