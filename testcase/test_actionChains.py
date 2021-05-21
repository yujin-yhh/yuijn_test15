from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        url = "http://sahitest.com/demo/clicks.htm"
        self.driver.get(url)

    def teardown(self):
        self.driver.quit()

    # 分布写法
    def test_case_actions(self):
        element_dbclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_clear = self.driver.find_element_by_xpath('//input[@value="Clear"]')
        actions = ActionChains(self.driver)
        actions.double_click(element_dbclick)
        actions.click(element_clear)
        actions.perform()

    # 链式写法
    def test_action_chain(self):
        element_dbclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_clear = self.driver.find_element_by_xpath('//input[@value="Clear"]')
        ActionChains(self.driver).double_click(element_dbclick).perform()

    def test_drag(self):
        old_ele = self.driver.find_element(By.XPATH, '//*[@title="from"]')
        new_ele = self.driver.find_element(By.XPATH, '//*[@title="to"]')
        actions = ActionChains(self.driver)
        # 第一种方式实现拖拽
        actions.drag_and_drop(old_ele, new_ele).perform()
        # 第二种方式实现拖拽
        actions.click_and_hold(old_ele).release(new_ele).perform()
        # 第三种凡事实现拖拽
        actions.click_and_hold(old_ele).move_to_element(new_ele).release().perform()