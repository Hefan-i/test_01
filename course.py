#!/usr/bin/python
# coding=utf-8
import sys
sys.path.append('/Users/jlg1128/PycharmProjects/ykt_web')
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

url='https://ke.study.163.com/course/detail/100091988'
driver=webdriver.Chrome("/Applications/chromedriver")
driver.get(url)
time.sleep(1)
[

    '/html/body/div[4]/div[1]/div[2]/div/p[2]'
]
   #关闭协议同意
agree=driver.find_element_by_xpath('//*[@id="ux-modal"]/div[3]/span')
agree.click()
time.sleep(3)

# a=driver.find_element_by_xpath('//*[@id="mod-course-head"]/div[2]/div/p[1]')
# b=driver.find_element_by_xpath('//*[@id="mod-course-head"]/div[2]/div/p[2]')
# c=driver.find_element_by_xpath('//*[@id="mod-course-head"]/div[2]/div/p[3]')
# d=driver.find_element_by_xpath('//*[@id="mod-course-head"]/div[2]/div/p[4]')
# print(a.text)
# print(b.text)
# print(c.text)
# print(d.text)
#
# status=driver.find_element_by_class_name('course-status')
# print(status.text)
# url1=driver.find_element_by_xpath('//*[@id="mod-course-head"]/div[2]/div/dl/dd/a[1]').get_attribute("href")
# url2=driver.find_element_by_xpath('//*[@id="mod-course-head"]/div[2]/div/dl/dd/a[2]').get_attribute('href')
# print(url1,url2)


# prcie1=driver.find_element_by_class_name('price')
# print(prcie1.text)
# time1=driver.find_element_by_id('time-countdown2').get_attribute('data-end')
# print(time1)

# qian=driver.find_element_by_class_name('course-set-item-title')
# print(qian.text)
# gou=driver.find_element_by_id('courseSetItemBtn').get_attribute('data-package')
# print(gou)
#更多课程
# gengduo=driver.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[2]/div[3]/a/p')
# print(gengduo.text)
# more_price=driver.find_element_by_xpath('//*[@id="side_recommends"]/a/span')
# print(more_price.text)
# more_courl=driver.find_element_by_class_name('course-summary-puretext').get_attribute('href')
# print(more_courl)

#课程表
# dianji=driver.find_element_by_css_selector('a[data-tb="con-catalog"]')
# print(dianji.text)
# dianji.click()
#
# yiji=driver.find_element_by_class_name('_2twj')
# print(yiji.text)
# erji=driver.find_element_by_class_name('_3URt')
# print(erji.text)
# banxuename=driver.find_element_by_class_name('_1zb')
# print(banxuename.text)
#
# ke=ActionChains(driver)
# ke.move_to_element(banxuename).perform()
# # time.sleep(2)
# xuyao=driver.find_element_by_class_name('_2dyh')
# print(xuyao.text)
#
# banxue2=driver.find_element_by_class_name('_3DNW')
# print(banxue2.text)
pingjia=driver.find_element_by_css_selector('a[data-tb="con-comment"]')
print(pingjia.text)

pingjia.click()
time.sleep(2)
history=driver.find_element_by_css_selector('a[data-tb="comment-history"]')
history.click()
pinglun=driver.find_element_by_xpath("//div[@id='comment-history']/ul/li/div/div[@class='c-words']")
print(pinglun.text)

now=driver.find_element_by_css_selector('a[data-tb="comment-current"]')
now.click()
time.sleep(1)
history=driver.find_element_by_class_name('c-words')
print(history.text)
driver.quit()