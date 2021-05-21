from appium import webdriver


class BasePage():
    def __init__(self, driver: webdriver = None):
        # 初始化，接收driver
        self.driver = driver

    def find(self, by, locator):
        self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def find_and_sendkeys(self, by, locator, text):
        self.driver.find_element(by, locator).send_keys(text)

    def find_scroll_text_click(self, text):
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));').click()

    def find_text(self, by, locator):
        return self.driver.find_element(by, locator).text

    def find_text_second(self):
        pass

