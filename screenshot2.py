#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import HTMLTestReport
import HTMLTestRunner
import os,sys,time
import unittest
import codecs
from selenium import webdriver

current_day = time.strftime("%Y-%m-%d", time.localtime(time.time()))

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # self.base_url = "https://www.baidu.com"
        # self.driver.get(self.base_url)
        self.driver.get("https://www.baidu.com")
 
    def test_case1(self):
        """設計測試失敗case"""  # *****效果是在測試報告中顯示顯示出測試名稱*****
        print("========【case_0001】打開百度搜索 =============")
        # current_time = time.strftime("%Y-%M-%D-%H-%M-%S", time.localtime(time.time()))
        # "."表示創建的路徑為當.py文件所處的地址，\\是用\將“\”轉義
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = 'C:\\selenium\\result\\' +current_day+'\\'+current_time+'.png'
        print(pic_path)  # 打印圖片的地址
        time.sleep(5)
        self.driver.save_screenshot(pic_path)  # 截圖，獲取測試結果
        self.assertEqual('百度一下，你就知道', self.driver.title)  # 斷言判斷測試是否成功,判斷標題是否為百度(設計失敗的case)
 
    def test_case2(self):
        """設計測試過程中報錯的case"""
        print("========【case_0002】搜索selenium =============")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id('su').click()
        time.sleep(5)
        # current_time = time.strftime("%Y-%M-%D-%H-%M-%S", time.localtime(time.time()))
        # "."表示創建的路徑為當.py文件所處的地址，\\是用\將“\”轉義
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = 'C:\\selenium\\result\\' +current_day+'\\'+current_time+'.png'
        print(pic_path)  # 打印圖片的地址
        time.sleep(5)
        self.driver.save_screenshot(pic_path)  # 截圖，獲取測試結果
        self.assertIn('selenium', self.driver.title)  # 斷言書寫錯誤，導致case出錯
 
    def test_case3(self):
        """設計測試成功的case"""
        print("========【case_0003】 搜索夢雨情殤博客=============")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys("夢雨情殤")
        self.driver.find_element_by_id('su').click()
        # "."表示創建的路徑為當.py文件所處的地址，\\是用\將“\”轉義
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = 'C:\\selenium\\result\\' +current_day+'\\'+current_time+'.png'
        print(pic_path)  # 打印圖片的地址
        time.sleep(5)
        self.driver.save_screenshot(pic_path)  # 截圖，獲取測試結果
        self.assertIn('夢雨情殤', self.driver.title)
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == "__main__":
     file_path = 'C:\\selenium\\result\\'+ current_day
     if os.path.exists(file_path):
        print("路徑存在。")
     else:
        print("路徑不存在。")
        os.mkdir(file_path)
        print("create successfully")
     '''生成測試報告'''
     testunit = unittest.TestSuite() # 定義一個單元測試容器
     testunit.addTest(Baidu("test_case1")) #將測試用例加入到測試容器內
     testunit.addTest(Baidu("test_case2"))
     testunit.addTest(Baidu("test_case3"))
     current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
     report_path = 'C:\\selenium\\result\\'+current_day+'SoftTestReport_' + current_time + '.html'  # 生成測試報告的路徑
     fp = open(report_path, 'wb')
     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自動化測試報告", description='測試報告')
     # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自動化測試報告", description='自動化測試演示報告')
     runner.run(testunit)
     fp.close()