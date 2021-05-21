from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.basepages.basepage import BasePage
from web.pages.addmember_page import AddMemberPage


class ContactPage(BasePage):

    def goto_addmember(self):
        # 定位添加成员按钮并点击
        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) a:nth-child(2)")
        # element: WebElement = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # element.click()

        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, "username")
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)

        return AddMemberPage(self.driver)

    def get_memberlist(self):
        self.driver.refresh()
        member_title = []
        elements = self.finds(By.CSS_SELECTOR, ".ui-sortable-handle>td:nth-child(2)")
        for element in elements:
            member_title.append(element.get_attribute("title"))
        print(member_title)
        return member_title
