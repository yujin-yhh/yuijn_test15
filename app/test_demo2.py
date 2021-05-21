from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemoTwo:

    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "test",
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.ApiDemos",
            "noReset": "true"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_webview(self):
        view = "WebView"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Views']").click()
        print(self.driver.contexts)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{view}").instance(0));').click()
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID, 'i am a link').click()
