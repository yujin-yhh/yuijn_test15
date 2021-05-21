from appium.webdriver.common.mobileby import MobileBy

from app.pages.base_page import BasePage


class ContactAddPage(BasePage):

    # def __init__(self, driver):
    #     # 初始化，接收driver
    #     self.driver = driver

    def contact_add(self, name, gender, phonenum):
        """
        添加联系人
        :return:
        """
        # 定位姓名，并输入
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys(name)
        # 点击性别，并选择对应的性别
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[contains(@text,'男')]").click()

        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        # 定位手机号，并输入
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'手机')]/..//*[contains(@class,'EditText')]").send_keys(phonenum)
        # 滑动，点击保存按钮
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("保存").instance(0));').click()

        from app.pages.memberInviteMenu_page import MemberInviteMenuPage

        return MemberInviteMenuPage(self.driver)
