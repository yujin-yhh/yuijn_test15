from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.basepages.basepage import BasePage
from web.pages.registe_page import RegisterPage


class LoginPage(BasePage):

    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    # 扫描二维码登录
    def scan(self):
        pass

    # 点击企业注册
    def goto_register(self, driver: WebDriver):
        # 点击立即注册按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # 跳转到注册页面
        return RegisterPage(self.driver)
