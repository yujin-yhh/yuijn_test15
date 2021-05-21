from app.app.app import App


class TestAddContact():

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addContact(self):
        name = "yujin005"
        gender = "女"
        phonenum = "13209091235"
        result = self.main.goto_addMember().click_addContact().goto_contactAddManual(). \
            contact_add(name, gender, phonenum).get_toast()
        assert "添加成功" == result