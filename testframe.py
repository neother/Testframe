import datetime
import os

from selenium import webdriver

path = '/Users/qit/documents/webdriver/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get('http://baidu.com')
input = driver.find_element_by_id('kw')
input.send_keys('H 漫画')
click = driver.find_element_by_id('su')
click.click()

