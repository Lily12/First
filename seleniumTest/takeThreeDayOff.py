# takeThree
# 2021/2/28
# create by grace hu

import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import waitTool
# 创建浏览器驱动
driver = webdriver.Chrome(r'/usr/local/bin/chromedriver')
# 隐式等待
driver.implicitly_wait(10)
#访问网址
driver.get('http://192.168.1.42:8088/')
#登陆输入登陆名密码,点击登陆
driver.find_element_by_name('username').send_keys('libai')
driver.find_element_by_name('password').send_keys('opmsopms123')
# driver.find_element_by_tag_name('button').click()
driver.find_element_by_css_selector('#login-form > div.login-wrap > button').click()
#点击审批管理
driver.find_element_by_xpath('//ul[@class="nav nav-pills nav-stacked custom-nav js-left-nav"]/li[4]').click()
#请假
driver.find_element_by_xpath('//a[@href="/leave/manage"]').click()
time.sleep(3)
#请假申请
driver.find_element_by_xpath('//a[@href="/leave/add"]').click()
#请假类型
driver.find_element_by_xpath('//select[@name="type"]/option[@value="1"]').click()
time.sleep(2)
startTime = (datetime.date.today()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')
endTime = (datetime.date.today()+datetime.timedelta(days=4)).strftime('%Y-%m-%d')
# print(startTime,endTime)
#开始时间
sele = driver.find_element_by_xpath('//input[@name="started"]')
sele.click()
sele.send_keys(Keys.CONTROL, 'a')
sele.send_keys(Keys.DELETE)
sele.send_keys(startTime)
time.sleep(2)
#结束时间
eele = driver.find_element_by_xpath('//input[@name="ended"]')
eele.click()
eele.send_keys(Keys.CONTROL, 'a')
eele.send_keys(Keys.DELETE)
eele.send_keys(endTime)
time.sleep(2)
#请假天数
days = driver.find_element_by_name('days')
days.click()
days.clear()
# days.send_keys(Keys.CONTROL,'a')
# days.send_keys(Keys.DELETE)
days.send_keys(3)
time.sleep(2)
#请假事由
driver.find_element_by_name('reason').send_keys('如世界很大，我想出去走一走')
time.sleep(2)
#滑动web界面
driver.execute_script("window.scrollBy(0, 1000);")#向下滑动
#选择审核人
driver.find_element_by_xpath('//a[@href="#acceptModal"]').click()
time.sleep(2)
# driver.find_element_by_xpath('//a[@data-name="张三"]').click()
shlist = driver.find_elements_by_xpath('//div[@class="modal-body"]/ul/li')
num = randint(0, len(shlist)-1)
print(num)
shlist[num].click()
time.sleep(1)
# driver.find_element_by_xpath('//button[@type="submit"]').click()