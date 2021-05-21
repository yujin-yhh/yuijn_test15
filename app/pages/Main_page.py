from appium.webdriver.common.mobileby import MobileBy

from app.pages.base_page import BasePage
from app.pages.contactList_page import ContactListPage
from app.pages.memberInviteMenu_page import MemberInviteMenuPage


class MainPage(BasePage):

    def goto_message(self):
        """
        进入消息页
        :return:
        """
        pass

    def goto_addMember(self):
        """
        点击通讯录，进入通讯录页面
        :return:
        """
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录']")
        return ContactListPage(self.driver)
