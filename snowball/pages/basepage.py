import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from snowball.pages.handle_black import handle_blacklist


class BasePage:
    # 定义黑名单
    black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/ib_close']"),
                  (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    # 设置计数器
    error_num = 0
    max_num = 3

    def __init__(self, driver: WebDriver = None):
        """
        初始化driver
        """
        if driver == None:
            caps = {
                "platformName": "android",
                "deviceName": "snowball",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".common.MainActivity",
                "noReset": "true",
                "dontStopAppOnReset": "true"
            }
            self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def goto_main(self):
        """
        跳转到首页
        :return:
        """
        from snowball.pages.mainpage import MainPage
        return MainPage(self.driver)

    @handle_blacklist
    def find(self, by, locator=None):
        """
        封装元素查找方法
        :param by:
        :param locator:
        :return:
        """

        if locator == None:
            # 如果参数只有by
            result = self.driver.find_element(*by)
        else:
            # 如果参数既有by，又有locator
            result = self.driver.find_element(by, locator)
        # 如果能找到该元素，则将错误次数清0
        self.error_num = 0
        return result

    def wait_and_find(self, by, locator=None):
        """
        封装显示等待
        :return:
        """
        if locator == None:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by))

        else:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((by, locator)))
        return self.find(by, locator)

    def parse_yaml(self, path, func_name):
        """
        解析文件，调用解析步骤方法
        :return:
        """
        with open(path) as f:
            data = yaml.load(f)
        self.parse(data[func_name])

    def parse(self, steps):
        """
        解析步骤
        :param steps:
        :return:
        """
        for step in steps:
            if 'click' == step["action"]:
                self.find(step['by'], step['locator']).click()
            elif 'send' == step["action"]:
                self.wait_and_find(step['by'], step['locator']).send_keys(step["text"])
