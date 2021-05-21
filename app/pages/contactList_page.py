from app.pages.base_page import BasePage
from app.pages.memberInviteMenu_page import MemberInviteMenuPage


class ContactListPage(BasePage):

    def click_addContact(self):
        """
        点击添加成员
        :return:
        """
        # 滑动查找 添加成员 并点击
        # self.driver.find_element_by_android_uiautomator(
        #     'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()

        self.find_scroll_text_click("添加成员")
        return MemberInviteMenuPage(self.driver)
