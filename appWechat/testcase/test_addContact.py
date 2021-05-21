from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddContact():

    def setup(self):
        cap_disire = {
            "platformName": "android",
            "deviceName": "hogwarts",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "noReset": "true",
            "dontStopAppOnReset": "true"
        }
        self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", cap_disire)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_addContact(self):
        hog_name = 'Yujinb'
        hog_gender = '女'
        hog_phone = '13098909802'
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滑动查找，点击 添加成员
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        # 点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 定位姓名，并输入
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys(hog_name)
        # 点击性别，并选择对应的性别
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[contains(@text,'男')]").click()
        if hog_gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        # 定位手机号，并输入
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'手机')]/..//*[contains(@class,'EditText')]").send_keys(hog_phone)
        # 滑动点击保存按钮
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("保存").instance(0));').click()
        # sleep(2)
        result = self.driver.find_element(MobileBy.XPATH, "//*[contains(@class,'Toast')]").text
        # print(self.driver.page_source)
        assert "添加成功" == result
