#selenium获取Cookie
from selenium import webdriver
import time
import json
from ppring import pprint

post={}

driver=webdriver.Chrome(executable_path=' ')
driver.get('http://mp.weixin.qq.com/')
time.sleep(2)
driver.find_element_by_xpath("./*//input[@id='account']").clear()
driver.find_element_by_xpath("./*//input[@id='account']").send_keys('你的账号？')
driver.find_element_by_xpath("./*//input[@id='pwd']").clear()
driver.find_element_by_xpath("./*//input[@id='pwd']").send_keys('你的密码？')

time.sleep(5)
driver.find_element_by_xpath("./*//a[@id='loginBT']").click()

time.sleep(15)
driver.get('http://mp.weixin.qq.com/')
cookie_items=driver.get_cookies()
for cookie_item in cookie_items
	post[cookie_item['name']]=cookie_item['value']
cookie_str=json.dumps(post)
with open('cookie.txt','w+',encoding='utf-8')  as f:
   f.write(cookie_str)