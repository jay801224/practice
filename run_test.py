#coding:utf-8
from HTMLTestRunner import HTMLTestRunner
import unittest
import time

test_dir = 'C:/selenium/test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='uat*.py')


# #构造测试集
# def Suite():
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(test_baidu.MyTest))
#     suite.addTest(unittest.makeSuite(test_baidu_search.Search))
#     suite.addTest(unittest.makeSuite(test_baidu_translate.Baidutrans))
#     suite.addTest(unittest.makeSuite(test_login.LoginTest))

if __name__ == "__main__":
    runner = unittest.TestSuite()
    #导入当前时间，使用time模块的相关函数
    now=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
    #将测试结果写入到result.html中
    fp=open(now+"result.html",'wb')
    runner=HTMLTestRunner(stream=fp,title='Test Report',description='Result:')
    runner.run(discover)
    fp.close()

# if __name__=='__main__':
#     #执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)