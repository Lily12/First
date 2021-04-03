# notes
# 2021/3/9
# create by grace hu

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#封装显示等待
def webElementWait(driver,timeout,lo_time,by_locate,locate):
    '''
    :param driver: 驱动
    :param timeout: 最大等待时间
    :param lo_time: 轮询时间
    :param by_locate: 元素定位方法
    :param locate: 元素定位表达式
    :return: 元素对象
    '''
    return WebDriverWait(driver,timeout,lo_time).until(
        #设置等待条件
        EC.visibility_of_element_located(
            (by_locate,locate)
        )
    )

# 创建浏览器驱动
driver = webdriver.Chrome(r'/usr/local/bin/chromedriver')
# 隐式等待
driver.implicitly_wait(5)
#访问网址
driver.get('http://192.168.1.41:8088/')

#1.根据name 定位元素
driver.find_element_by_name('username')
#2.根据标签定位元素元素
driver.find_element_by_tag_name('button')
#3.根据class属性定位元素
'''根据class属性定位时，如果属性中间有空格，代表复合类，也就是具有多个class属性,
如：<p class='abc adb'>，class有两个值 abc adb，进行定位时任选一个值就可以了'''
driver.find_element_by_class_name('toggle-btn')
#4.根据链接文本定位元素
driver.find_elements_by_link_text('这是一个链接')
#5.根据链接文本模糊匹配进行定位元素
driver.find_element_by_partial_link_text('链接')
#6.根据xpath进行定位元素
driver.find_element_by_xpath('//button[@type="submit"]')
#7.根据css选择器定位元素
driver.find_element_by_css_selector('button')
#8.根据id定位元素
driver.find_element_by_id('login-form')

#返回的是一个列表
eles = driver.find_elements_by_css_selector('div.left-side-inner >ul>li')
#调用显示等待
ele = webElementWait(driver, 10, 0.5, By.NAME, 'username')

#xpath绝对路径,从html最顶层一层层的往下写
driver.find_element_by_xpath('/html/body/section/div[1]/div[3]/ul/li[1]/a/span')
#xpath相对路径，以//开头，可以匹配文档的任意一层
driver.find_element_by_xpath('//i[@class="fa fa-home"]')
#xpath以.表示当前路径
driver.find_element_by_xpath('//i[@class="fa fa-home"]/.')
#xpath以..表示上层路径
driver.find_element_by_xpath('//i[@class="fa fa-home"]/..')
#可以使用下标进行辅助定位，下标是从1开始的
driver.find_element_by_xpath('//ul[@class="nav nav-pills nav-stacked custom-nav js-left-nav"]/li[1]')
#定位列表最后一个
driver.find_element_by_xpath('//ul[@class="nav nav-pills nav-stacked custom-nav js-left-nav"]/li[last()]')
#定位列表倒数第二个
driver.find_element_by_xpath('//ul[@class="nav nav-pills nav-stacked custom-nav js-left-nav"]/li[last()-1]')
#xpath用*表示任意节点
driver.find_element_by_xpath('//ul[@class="nav nav-pills nav-stacked custom-nav js-left-nav"]/*')
#xpath也可以根据属性进行定位，@
driver.find_element_by_xpath('//ul[@class="nav nav-pills nav-stacked custom-nav js-left-nav"]')
#可以不为属性指定值，以下表达式匹配所有具备id属性的li标签
driver.find_element_by_xpath('//li[@id]')
#可以匹配固定值的任意属性，匹配所有包含属性值等于abc的li元素，而不管属性是什么
driver.find_element_by_xpath('//li[*="abc"]')


#id选择器
driver.find_element_by_css_selector('#notice-box')
#class选择器
driver.find_element_by_css_selector('.fa-home')
#标签选择器（选择所有的button）
driver.find_element_by_css_selector('button')
#标签选择器可以和class选择器结合起来使用（选择class属性=fa-home的i标签）
driver.find_element_by_css_selector('i.fa-home')
#分组选择器，可以选中一组HTML元素(选择所有ul,li,a标签)
driver.find_element_by_css_selector('ul,li,a')
#属性选择器,选择title="xxx"的所有元素
driver.find_element_by_css_selector('[title="xxx"]')
#也可以不为属性指定值，定位所有有name属性的元素
driver.find_element_by_css_selector('[name]')
#也可以为属性指定标签类型，定位所有有name属性的p标签
driver.find_element_by_css_selector('p[name]')
#组合选择符，子元素选择器，只能选取父元素的直接子元素
driver.find_element_by_css_selector('div.profile-desk>h1>a[href="/my/task"]')
#后代选择器用于选取某元素的后代元素
driver.find_element_by_css_selector('div.profile-desk a[href="/my/task"]')
#相邻兄弟选择器，可选择紧挨在某元素之后的一个元素 id=xyz后面的class属性为xx
driver.find_element_by_css_selector('#xyz + .xx')
#后续兄弟选择器，可选择某元素之后的所有元素
driver.find_element_by_css_selector('#xyz ~ .xx')

#设置窗口大小
driver.set_window_size(600, 600)
#最小化浏览器
driver.minimize_window()
#最大化浏览器
driver.maximize_window()
#浏览器后退
driver.back()
#浏览器前进
driver.forward()
#页面刷新
driver.refresh()

ele = driver.find_elements_by_name('username')
ele.text
ele.size
ele.get_attribute("class")

from selenium.webdriver.common.keys import Keys
#全选
ele.send_keys(Keys.CONTROL, 'a')
#剪切
ele.send_keys(Keys.CONTROL, 'x')
#删除
ele.send_keys(Keys.DELETE)
#退格键
ele.send_keys(Keys.BACKSPACE)
#空格
ele.send_keys(Keys.SPACE)
#esc
ele.send_keys(Keys.ESCAPE)

from selenium.webdriver.common.action_chains import ActionChains
#鼠标悬停操作
ActionChains(driver).move_to_element(ele).perform()
#右击
ActionChains(driver).context_click(ele).perform()
#左键单击
ActionChains(driver).click(ele).perform()
#双击
ActionChains(driver).double_click(ele).perform()
#鼠标拖拽 将元素1拖拽到元素2
ActionChains(driver).drag_and_drop(ele,ele).perform()

#截屏 截取整个页面,保存为1.png
driver.get_screenshot_as_file("./1.png")
#截屏 截取单个元素,保存为2.png
driver.find_element_by_css_selector('button').screenshot('./2.png')

#对话框（只有确认按钮）
al = driver.switch_to.alert
al.accept()#确认按钮
#确认框（有确认和取消）
al = driver.switch_to.alert
al.accept()#确认
al.dismiss()#取消
#提示框（有提示语）
al = driver.switch_to.alert
al.send_keys('这是一段提示与')
al.accept()#确认
al.dismiss()#取消


#获取浏览器中当前打开所有标签的句柄
allHandles = driver.window_handles
#切换到title='****'的标签页
for handle in allHandles:
    driver.switch_to.window(handle)
    if driver.title == '****':
        break

#找到内嵌网页
ifm = driver.find_elements_by_css_selector('.ke-edit-iframe')
#切换到内嵌网页
driver.switch_to.frame(ifm)
#在内嵌网页中进行操作
pass
#回到外层
driver.switch_to.default_content()
