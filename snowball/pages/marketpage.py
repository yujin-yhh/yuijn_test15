from appium.webdriver.common.mobileby import MobileBy

from snowball.pages.basepage import BasePage
from snowball.pages.searchpage import SearchPage


class MarketPage(BasePage):

    def goto_search(self):
        """
        跳转到搜索页面
        :return:
        """
        # 定位搜索框，并点击
        # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        # self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.parse_yaml("marketpage.yaml", "goto_search")
        return SearchPage(self.driver)
