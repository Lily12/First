# waitTool
# 2021/3/1
# create by grace hu
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

def webElementWait(driver, timeout, lo_time, by_locate, locate):
    '''
    :param driver:
    :param timeout:最大等待时间
    :param lo_time:轮询时间
    :param by_locate:元素定位方法
    :param locate:元素定位表达式
    :return:元素对象
    '''
    return WebDriverWait(driver, timeout, lo_time).until(
        #设置等待条件
        EC.visibility_of_element_located(
            by_locate, locate
        )
    )
