from selenium import webdriver
from selenium.webdriver.common.by import By

from web.podemo.login_page import LoginPage
from web.podemo.registe_page import RegisterPage


class IndexPage():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    # 进入到登录页面
    def goto_login(self):
        # 点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # 跳转到登录页面
        return LoginPage(self.driver)

    # 进入到注册页面
    def goto_register(self):
        # 点击注册按钮，
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # 跳转到注册页面
        return RegisterPage(self.driver)
