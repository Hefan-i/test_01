# -*- coding: UTF-8 -*-
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url='https://study.163.com/'
driver=webdriver.Chrome("/Applications/chromedriver")
driver.get(url)
time.sleep(3)
   #关闭协议同意
agree=driver.find_element_by_xpath('//*[@id="ux-modal"]/div[3]/span')
agree.click()
    #关闭类目选择
closeCg=driver.find_element_by_xpath('//*[@id="ux-modal"]/div[1]/a/i')
closeCg.click()
time.sleep(3)

  #选择登陆框
selectLg=driver.find_element_by_id('j-nav-login')
#击这个button的时候，这个单击事件被上层的div给接收了……说明div覆盖在这个button上面
driver.execute_script("arguments[0].click();", selectLg)
time.sleep(5)
# emial=driver.find_element_by_xpath('//*[@class="ux-tabs-underline_hd"]/li[2]')
# emial=driver.find_elements_by_css_selector("ul.ux-tabs-underline_hd > li")
emial = driver.find_element_by_css_selector("ul.ux-tabs-underline_hd > li:nth-child(2)")
emial.click()

#遇到嵌套的frame，切进去，frame的id随机，所有找到父节点对应的class中找到iframe标签
def switch(a):
    # 判断该frame是否可以switch进去,如果直接传入定位方式id，可以的话就返回True并switch进去，否则返回False

         WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(a))
iframe = driver.find_element_by_xpath('//*[@id="j-ursContainer-0"]').find_element_by_tag_name('iframe')
switch(iframe)
# iframe=driver.find_element_by_xpath('//*[@id="j-ursContainer-1"]').find_element_by_tag_name('iframe')
# driver.switch_to.frame(iframe)
#
# user=driver.find_element_by_id('phoneipt')
# user.send_keys('13095828875')
# pw=driver.find_element_by_class_name('j-inputtext')
# pw.send_keys('qa123456')
#邮箱登录
# emial=driver.find_element_by_xpath('//*[@class="ux-tabs-underline_hd"]')

#邮箱账号密码输入框
email_account=driver.find_element_by_class_name('dlemail')

email_account.send_keys('ad_ykt_adlt_021d@163.com')
pwt=driver.find_element_by_class_name('dlpwd')
pwt.send_keys('bLfNX1p8')

# login=driver.find_element_by_id('submitBtn')
login=driver.find_element_by_id('dologin')
login.click()
#frame中切回主文档
# driver.switch_to.default_content()
# time.sleep(3)
#
# myclass=driver.find_element_by_id('j-nav-my-class')
# myclass.click()
# time.sleep(5)
#
# classtime=driver.find_element_by_class_name('mystudy-course-card-header_desc')
# print(classtime.text)
# Courseprogress=driver.find_element_by_class_name('mystudy-course-card-title-learned')
# print(Courseprogress.text)

# yktTag=driver.find_element_by_class_name('tips').get_attribute('href')
# print(yktTag)
# learn=driver.find_element_by_class_name('mystudy-course-card-footer')
# print(learn.text)
# 置顶操作
# card=driver.find_element_by_class_name('mystudy-course-card-title_name')
# ke=ActionChains(driver)
# ke.move_to_elementd).perform()
# time.sleep(2)
#
# ziding=driver.find_element_by_class_name('course-top')
# ziding.click()

#搜索操作
# sousuo=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/label')
# sousuo.send_keys('测试')
# sou=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/span')
# sou.click()
# time.sleep(3)
# coure=driver.find_element_by_class_name('mystudy-course-card-title_name')
# a=coure.text
# print(a)
# print(a.find("测试"))

# work=driver.find_element_by_class_name('myclass-head_vipEnter').get_attribute('href')
# print(work)
print("lalalalal")