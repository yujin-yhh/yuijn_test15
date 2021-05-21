from appium.webdriver.common.mobileby import MobileBy

from app.pages.base_page import BasePage
from app.pages.contactAdd_page import ContactAddPage


class MemberInviteMenuPage(BasePage):

    def goto_contactAddManual(self):
        """
        点击手动输入添加，进入添加成员页面
        :return:
        """
        # 点击手动添加
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")

        return ContactAddPage(self.driver)

    def get_toast(self):
        # result = self.driver.find_element(MobileBy.XPATH, "//*[contains(@class,'Toast')]").text
        result = self.find_text(MobileBy.XPATH, "//*[contains(@class,'Toast')]")
        return result
