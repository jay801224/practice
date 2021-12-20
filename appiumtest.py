# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformVersion"] = "10.0"
caps["deviceName"] = "one plus 6"
caps["platformName"] = "Android"
caps["automationName"] = "Appium"
caps["app"] = "\\appium_demo\\Carrefour.apk"
caps["autoAcceptAlerts"] = "true"
caps["noReset"] = "true"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.implicitly_wait(30)
el1 = driver.find_element_by_id("com.carrefour.carrefourapp:id/toolBarInclude_rightImageView")
driver.implicitly_wait(30)
el1.click()
el2 = driver.find_element_by_id("com.carrefour.carrefourapp:id/toolBarInclude_leftImageView")
el2.click()
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView")
el3.click()
el4 = driver.find_element_by_id("com.carrefour.carrefourapp:id/productDetailFragment_specificationIntroductionConstraintLayout")
el4.click()
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[1]")
el5.click()
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup[3]/android.support.v7.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView[2]")
el6.click()
el7 = driver.find_element_by_id("com.carrefour.carrefourapp:id/loginFragment_facebookImageView")
el7.click()

driver.quit()