import shelve
import time
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(3)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]').click()

        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1

        # until的参数可以上传一个方法，所以定义了一个方法wait，注意方法作为参数传递的时候不能加()，否则是调用
        # 但是until传参的方法有一个参数，所以在定义wait()方法时传递了一个参数
        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()

    @pytest.mark.skip
    def test_getcookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        # self.driver.find_element(By.CSS_SELECTOR, ".nav-bar-links>div:nth-child(2)").click()

    @pytest.mark.skip
    def test_fuyong(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # self.driver.find_element(By.CSS_SELECTOR, ".nav-bar-links>div:nth-child(2)").click()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851926895696'}, {'domain': '.work.weixin.qq.com', 'expiry': 1651045506, 'httpOnly': False,
                                            'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
                                            'secure': False, 'value': '1619508613,1619509506'},
            {'domain': '.qq.com', 'expiry': 1928990749, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '1_1158501442'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'OQZl52qI6iM6EuX7ipLELOdZJv6CspU2_q_iJcj0V2wDUIO55NzL7X1rZLGd16J-945NEpVBZaxB0fvhhj1WpBNvhmAgUabs6sH1F6F7DgIuv7_OlzHyPOT6mzOPD6Kpq4IPIpWrHKSHGjhudVyyGPD4l0B1iEVM4TqkB8nOHl9eS2LCiu9eMPXyVdns5kPXIdynnCtVCo2mo7NhotRFtR2mr1BVa63c34lJw5iL6gp5XFOUGhVlHAoi8E6VPjWwSwTAIaz79PNTiAmWUEDG5A'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851926895696'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '3566793555'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '6131460096'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325041161079'},
            {'domain': '.qq.com', 'expiry': 1619658251, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.483678035.1619508613'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'uw8k93GR_IIL9PC_b_e0NRyFmEPXxR6Oyn15Cd0-Ga_bm5JB3-3hwzMrh5M4osHc'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a7991049'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '272860607113724'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1619603364, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '529teco'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': False, 'value': '1158501442'},
            {'domain': '.qq.com', 'expiry': 2147483670, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '3218890a33ab9267480a265c70e8350ebcb8e76aad1ceb915ff27d1e30414893'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'u2hRk5OCF/'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1638930680, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1928201560, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': 'd751b5177702946b'},
            {'domain': '.qq.com', 'expiry': 1619571888, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1682643851, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1015446159.1607394682'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1622163854, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'}]
        # 打开页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # add_cookie可以把cookie添加到当前的页面中去
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 重新访问此页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # 或者刷新页面
        # self.driver.refresh()
        sleep(2)

    def test_shelve(self):
        # 打开数据库，此处的cookie是文件名
        db = shelve.open("cookie")
        # 从shelve中读取数据添加到变量cookie中，db["cookie"]中的cookie是数据文件中到key值
        cookies = db["cookie"]
        # print(cookies)
        # 打开浏览器
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # 将cookie添加到页面中
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 刷新页面
        self.driver.refresh()
