import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class LoginTests(unittest.TestCase):

    def setUp(self):
        app = ('/Users/lawrey/Library/Developer/Xcode/DerivedData/AppiumTest-fubxvjmcpxiewkenopxpcerwhudw/Build/Products/Debug-iphonesimulator/AppiumTest.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '11.4',
                'deviceName': 'iPhone 6s'
            }
        )