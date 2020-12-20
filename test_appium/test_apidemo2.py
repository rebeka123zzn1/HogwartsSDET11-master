# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import json
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        """



        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        # caps["skipServerInstallation"] = True
        # caps["chromedriverExecutableDir"]="/Users/seveniruby/projects/chromedriver/all"
        # caps["chromedriverExecutable"] = "/Users/seveniruby/projects/chromedriver/all/chromedriver_2.20"
        caps[
            "chromedriverExecutable"] = "/Users/seveniruby/projects/chromedriver/chromedrivers/chromedriver_74.0.3729.185"

        # caps['avd'] = 'Pixel_2_API_23'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)
        # try:
        #     self.driver.find_element(By.XPATH, "//*[@text='同意']").click()
        # finally:
        #     pass

        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located())
         """

        caps = {}
        caps["platformName"] = "Android"
        caps["automationName"] = "uiautomator2"
        caps["deviceName"] = "xiaomi-mi_5s-238c8e2f"
# """hogwarts"

        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["noReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_toast(self):
        pass

    def teardown(self):
        pass
        # sleep(20)
        # self.driver.quit()
