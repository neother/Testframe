import re
import threading
import time
import unittest
from selenium import webdriver
from logger import Logger
import HTMLTestRunner
import os
import sys
class SeleniumTestCase(unittest.TestCase):


    def setUp(self):
        options = webdriver.ChromeOptions()
      #  options.add_argument('headless')
        path = "/Users/qit/documents/webdriver/chromedriver"
        self.driver = webdriver.Chrome(executable_path=path,chrome_options=options)
        
        self.driver.get('http://baidu.com')

    def tearDown(self):
        time.sleep(3)

       # /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages
    
    def test_search1(self):
        # navigate to home page
       
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()

        self.assertTrue(re.search('selenium',self.driver.page_source))
'''
    def test_search2(self):
        self.driver.find_element_by_id('kw').send_keys('python')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()

        self.assertTrue(re.search('failed',self.driver.page_source))
'''
 
 
if __name__ =='__main__':

        # 设置报告文件保存路径
    report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
    # 获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    
    # 设置报告名称格式
    HtmlFile = report_path + now + "HTMLtemplate.html"
    fp = open(HtmlFile, 'wb')

    suite = unittest.TestLoader().discover("testframe")
        # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2)
    # 开始执行测试套件s
    runner.run(suite)
    fp.close()