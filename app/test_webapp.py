from time import sleep

from appium import webdriver


class TestWebApp:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "browserName": "Browser",
            "deviceName": "hogwarts",
            "noReset": "True",
            "udid": "emulator-5554",
            "newCommandTimeout": 300,
            "chromedriverExecutable": "/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver2-20"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(15)


    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        self.driver.find_element_by_id("index-bn").click()
        sleep(5)
