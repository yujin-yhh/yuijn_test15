from appium import webdriver

from app.pages.Main_page import MainPage
from app.pages.base_page import BasePage


class App(BasePage):

    def start(self):
        # 启动app
        if self.driver == None:
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
        else:
            self.driver.launch_app()
            # todo launch_app和start_activity的区别：
            # self.driver.start_activity()

        return self

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进入到首页
        return MainPage(self.driver)
