from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
import pytest
from appium import webdriver
# from selenium import webdriver

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "hogwarts",
            "appPackage": "com.xueqiu.android",
            "platformVersion": "6.0",
            "appActivity": "com.xueqiu.android.main.view.MainActivity",
            "newCommandTimeout": 300,
            "noReset": "true",
            "dontStopAppOnReset": "true"
            # "skipDevicesInitialization": "true"
            # "skipServerInstallation":'true'
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(15)

    def teardown(self):
        pass

    @pytest.mark.skip
    def test_attr(self):
        element = self.driver.find_element_by_id("com.xueqiu.android:id/scroll_view")
        print(element.get_attribute("text"))

    @pytest.mark.skip
    def test_scroll(self):
        sleep(10)
        action = TouchAction(self.driver)
        # 第一种方法，press("坐标点").move_to("移动到的坐标点").release()
        action.press(x=386, y=1048).wait(200).move_to(x=386, y=484).release().perform()

        # 第二种方法使用屏幕的相对位置
        # get_window_rect()获得屏幕尺寸，打印获得的值为{'width': 720, 'height': 1280, 'x': 0, 'y': 0}
        width = self.driver.get_window_rect()["width"]
        height = self.driver.get_window_rect()["height"]
        x1 = int(width / 2)
        y_start = height * 0.8
        y_end = height * 0.4
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

        sleep(3)

    @pytest.mark.skip
    def test_a(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_banner").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        sleep(3)

    @pytest.mark.skip
    def test_b(self):
        assert_that(10, equal_to(9), "this is a dialog")

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
        print("打印页面跳转前的contexts")
        print(self.driver.contexts)
        # print(self.driver.window_handles)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "免费领").click()
        print(self.driver.contexts)

        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.switch_to.context(self.driver.contexts[-1])
        sleep(3)
