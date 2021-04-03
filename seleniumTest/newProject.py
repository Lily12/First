# newProject
# 2021/3/4
# create by grace hu
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# 隐式等待
driver.implicitly_wait(4)
#访问网址
driver.get('http://192.168.1.43:8088/')
driver.maximize_window()
#登陆输入登陆名密码,点击登陆
driver.find_element_by_name('username').send_keys('libai')
driver.find_element_by_name('password').send_keys('opmsopms123')
driver.find_element_by_css_selector('.btn').click()
#直接跳转到项目管理页
driver.get('http://192.168.1.43:8088/project/manage')
driver.find_element_by_link_text('+新项目').click()
#项目名称
proName = '自动化项目测试'
name = driver.find_element_by_name('name')
name.send_keys(Keys.COMMAND, 'a')
name.send_keys(Keys.COMMAND, 'x')
name.send_keys(proName)
#项目别名
proAliasName = '填海行动'
name = driver.find_element_by_name('aliasname')
name.send_keys(Keys.COMMAND, 'a')
name.send_keys(Keys.COMMAND, 'x')
name.send_keys(proAliasName)
time.sleep(1)
#项目开始时间
startTime = (datetime.date.today()+datetime.timedelta(1)).strftime('%Y-%m-%d')
endTime = (datetime.date.today()+datetime.timedelta(31)).strftime('%Y-%m-%d')
startTimeEle = driver.find_element_by_css_selector('[placeholder="开始日期"]')
startTimeEle.send_keys(Keys.COMMAND, 'a')
startTimeEle.send_keys(Keys.COMMAND, 'x')
startTimeEle.send_keys(startTime)
time.sleep(1)
#项目结束时间
endTimeEle = driver.find_element_by_css_selector('[placeholder="结束日期"]')
endTimeEle.send_keys(Keys.COMMAND, 'a')
endTimeEle.send_keys(Keys.COMMAND, 'x')
endTimeEle.send_keys(endTime)
time.sleep(2)
#项目描述
description = '这是一个任重而道远的项目，通过自动化的学习逐渐弥补自己的不足，像精卫学习，一块砖一块砖的搬'
ifm = driver.find_element_by_css_selector('.ke-edit-iframe')
driver.switch_to.frame(ifm)
driver.find_element_by_css_selector('.ke-content').send_keys(description)
driver.switch_to.default_content()
driver.find_element_by_css_selector('[type="submit"]').click()

# #case1：所有内容不填写，点击提交
# driver.execute_script('window.scrollBy(0, 1000);')
# time.sleep(1)
# driver.find_element_by_css_selector('[type="submit"]').click()
# time.sleep(1)
# driver.execute_script('window.scrollBy(0, -1000);')
# time.sleep(1)
# driver.get_screenshot_as_file('./shotPhoto/一个字段都未填写.png')

#case1：所有内容不填写，点击提交
# driver.execute_script('window.scrollBy(0, 1000);')
# time.sleep(1)
# driver.find_element_by_css_selector('[type="submit"]').click()
# time.sleep(1)
# driver.execute_script('window.scrollBy(0, -1000);')
# time.sleep(1)
# driver.get_screenshot_as_file('./shotPhoto/一个字段都未填写.png')

driver.find_element()