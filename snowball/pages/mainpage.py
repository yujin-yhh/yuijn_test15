import yaml
from appium.webdriver.common.mobileby import MobileBy

from snowball.pages.basepage import BasePage
from snowball.pages.marketpage import MarketPage


class MainPage(BasePage):

    def goto_market(self):
        """
        跳转到行情页面
        :return:
        """
        # 点击"笔"图标弹出黑名单页面
        # self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # # 使用封装后对find方法查找元素
        # self.find(MobileBy.XPATH, "//*[contains(@class,'TabWidget')]//*[contains(@text,'行情')]").click()
        # with open("mainpage.yaml") as f:
        #     datas = yaml.load(f)
        # steps = datas["goto_market"]
        # for step in steps:
        #     if 'click' == step["action"]:
        #         self.find(step['by'], step['locator']).click()
        self.parse_yaml("mainpage.yaml", "goto_market")

        return MarketPage(self.driver)
