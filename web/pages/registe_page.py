from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.basepages.basepage import BasePage


class RegisterPage(BasePage):

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    # 封装注册方法
    def register(self):
        # 定位到企业名称，并输入内容
        self.driver.find_element(By.ID, "corp_name").send_keys("aaaa")
        # 定位到管理员姓名，并输入内容
        self.driver.find_element(By.ID, "manager_name").send_keys("bbb")
        # 定位到手机号，并输入内容
        self.driver.find_element(By.ID, "register_tel").send_keys("13212341234")

        return True
