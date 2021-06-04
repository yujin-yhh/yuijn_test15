from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from snowball.pages.basepage import BasePage


class SearchPage(BasePage):

    def search(self):
        """
        封装搜索方法
        :return:
        """
        # 定位到输入框，并输入内容
        self.parse_yaml("searchpage.yaml","search")
        # locator = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']")
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        # self.driver.find_element(*locator).send_keys(text)
        # self.find(locator).send_keys(text)
        # self.find_and_sendkys(locator, text=text)
        # self.parse_yaml()
        # self.wait_and_find(locator).send_keys(text)
