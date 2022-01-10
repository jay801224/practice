# -*- coding: utf-8 -*-
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time

class test_twittertest(unittest.TestCase):

    def setUp(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument('--no-sandbox')
        options.add_argument("--window-position=0,0")
        options.add_argument('--window-size=1024,768')
        
        mobileEmulation = {"deviceName": "Nexus 5"}
        #手機要這行
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        #手機要這行

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    


    def testpcstart(self):
        driver = self.driver
        driver.get("https://www.twitch.tv/")
        time.sleep(3)
        
        #找搜尋框
        self.findsearch = driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/nav/div/div[2]/div/div/div/div/div/div/div/div/input")
        self.findsearch.click()
        self.findsearch.clear()
        #找關鍵字
        self.findsearch.send_keys("Monster Hunter World")
        self.findsearch.send_keys(Keys.ENTER)
        time.sleep(3)

        #findexpansionlist = driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div/div[2]/div/div[2]/button/div/div/div/div/p")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//p[contains(.,\'再顯示 5 個頻道\')]"): 
                    break
            except: 
                pass
            time.sleep(1)
        else: 
            self.fail("time out")
        self.findexpansionaddfive = driver.find_element(By.XPATH, "//p[contains(.,\'再顯示 5 個頻道\')]")
        #點第一次展開
        self.findexpansionaddfive.click()

        #等待第一次結果出現
        time.sleep(3)

        self.driver.execute_script("window.scrollTo(0,0)")
#          
# for i in range(10):
#             try:
#                 if self.is_element_present(By.XPATH, "//div[@id='root']/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div/div/div/div/div[5]/div/div/div/div/div/p"): break
#             except: pass
#             time.sleep(1)
#         else: 
#             self.fail("time out") 
# 
        
        #等待第二次更多按鈕出現
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//p[contains(.,\'顯示所有頻道\')]"): 
                    break
            except: 
                pass
            time.sleep(1)
        else: 
            self.fail("time out")
            
        #點第二次展開
        self.findexpansionaddmore = driver.find_element(By.XPATH, "//p[contains(.,\'顯示所有頻道\')]")
        self.findexpansionaddmore.click()
        
        #等待第二次結果出現
        time.sleep(3)

        #  for i in range(10):
        #     try:
        #         if self.is_element_present(By.XPATH, "//div[@id='root']/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div/div/div/div/div[9]/div/div/div/div/div/p"): break
        #     except: pass
        #     time.sleep(1)
        # else: 
        #     self.fail("time out")
        self.driver.execute_script("window.scrollTo(0,0)")

        #找不到題目所要求用戶，另找一個按過兩次展開的
        WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.LINK_TEXT, "不大行的幻哀音"), "不大行的幻哀音"))
        self.driver.find_element(By.LINK_TEXT, "不大行的幻哀音").click()


    def testmstart(self):
        driver = self.driver
        driver.get("https://m.twitch.tv/search")
        driver.set_window_size(889, 692)
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//input")))
        driver.find_element(By.XPATH, "//input").send_keys("Monster Hunter World")
        driver.find_element(By.CSS_SELECTOR, ".ScInputBase-sc-xgdj8u-0").send_keys(Keys.ENTER)
        time.sleep(1)
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(.,\'觀看全部\')]")))
        driver.find_element(By.XPATH, "//p[contains(.,\'觀看全部\')]").click()
        test_twittertest.scrolldown(self)
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".eZactg")))
        self.driver.find_element(By.XPATH, "//div[2]/div/div/button/div/div").click()
        time.sleep(3)
        self.driver.save_screenshot('video.png')
        
    
    def scrolldown (self):
        element = self.driver.find_element(By.XPATH, "//h4[contains(.,\'Mel_27\')]")
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.driver.get("https://m.twitch.tv/mel_27")
        time.sleep(3)

    def is_element_present(self, how, what):
        try: 
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: 
            return False
        return True
    
    def is_alert_present(self):
        try: 
            self.driver.switch_to_alert()
        except NoAlertPresentException as e: 
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: 
            self.accept_next_alert = True
    
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest = unittest.TestSuite()  
    #unittest.addTest(test_twittertest("testpcstart"))
    unittest.addTest(test_twittertest("testmstart"))

    #寫出測試報告
    fp = open("-twittertest.html", 'wb')
    runner = HTMLTestRunner(
        stream=fp, title='Test Report', description='Result:', tester='jay')
    runner.run(unittest)
    fp.close()