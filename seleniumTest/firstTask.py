# firstTask
# 2021/2/28
# create by grace hu
from seleniumTest import loginOpms
import time
from selenium import webdriver
# 创建浏览器驱动
driver = webdriver.Chrome(r'/usr/local/bin/chromedriver')
# 隐式等待
driver.implicitly_wait(10)
#访问网址
driver.get('http://192.168.1.41:8088/')
#登陆输入登陆名密码,点击登陆
driver.find_element_by_name('username').send_keys('libai')
driver.find_element_by_name('password').send_keys('opmsopms123')
# driver.find_element_by_tag_name('button').click()
driver.find_element_by_css_selector('#login-form > div.login-wrap > button').click()
#点击员工相册
# driver.find_element_by_css_selector('body > section > div.left-side.sticky-left-side > div.left-side-inner > ul > li:nth-child(6) > a > span').click()
driver.find_element_by_xpath('//ul[@class="nav nav-pills nav-stacked custom-nav js-left-nav"]/li[6]').click()
#点击油菜
ele = driver.find_element_by_link_text('油菜花')
ele = driver.find_element_by_xpath('//p/a[@href="/album/66621262012616704"]')
time.sleep(3)
ele.click()
#滑动web界面
driver.execute_script("window.scrollBy(0, 200);")#向下滑动
# driver.execute_script("window.scrollBy(0, -900);")#向上滑动
#点击评论按钮
driver.find_element_by_xpath('//a[@href="#commenta"]').click()
#定位评论输入框
driver.find_element_by_xpath('//textarea[@name="comment"]').send_keys('so beautiful1')
#提交评论
driver.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(5)
#退出浏览器
# driver.quit()