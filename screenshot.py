# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import os,sys,time
import HTMLTestReport
#登入
driver =webdriver.Firefox()
current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
current_day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
print(current_time)
print(current_day)
# 必須列印圖片路徑HTMLTestRunner才能捕獲並且生成路徑，\image\**\\**.png 是獲取路徑的條件,必須這樣的目錄
#設定儲存圖片路徑，測試結果圖片可以按照每天進行區分
#通過if進行斷言判斷
driver.get("https://baidu.com/")
#新建立路徑“.”表示當前整個.py檔案的路徑所在的位置，“\\”路徑分割符，其中的一個是“\”表示轉義字元
pic_path = 'C:\\selenium\\result\\'+current_day+'\\'+current_time+'.png'
print(pic_path)
file_path = 'C:\\selenium\\result\\'+ current_day
if os.path.exists(file_path):
  print("路徑存在。")
else:
  print("路徑不存在。")
  os.mkdir(file_path)
  print("create successfully")

time.sleep(5)
print(driver.title)
#擷取當前url頁面的圖片，並將擷取的圖片儲存在指定的路徑下面（pic_path），注：以下兩種方法都可以
driver.save_screenshot(pic_path)
# driver.save_screenshot('C:\\selenium\\result\\'+current_time1+'\\'+current_time+'.png') 
if u'百度一下，你就知道' == driver.title:
		print ('Assertion test pass.') 
else:
		print ('Assertion test fail.')
#通過try丟擲異常進行斷言判斷  
driver.get("https://baidu.com/")
driver.save_screenshot(pic_path)
try:
		assert u'百度一下，你就知道' == driver.title
		print ('Assertion test pass.') 
except Exception as e:
		print ('Assertion test fail.', format(e))
time.sleep(5)
driver.quit()
