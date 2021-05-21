from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.basepages.basepage import BasePage


class AddMemberPage(BasePage):

    def add_member(self, username, acctid, tel):
        # 输入姓名
        self.find(By.ID, "username").send_keys(username)
        # 输入账号
        self.find(By.ID, "memberAdd_acctid").send_keys(acctid)
        # 输入手机号
        self.find(By.ID, "memberAdd_phone").send_keys(tel)
        # 点击保存按钮
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()