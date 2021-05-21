from time import sleep

from web.pages.index_page import IndexPage


class TestWX:

    def setup(self):
        self.index = IndexPage()

    def test_registe(self):
        assert self.index.goto_register().register()

    def test_addcontact(self):
        username = "hogwarts007"
        acctid = "acctid_hogwarts007"
        tel = "13212341007"
        addmember = self.index.goto_contact()
        addmember.goto_addmember().add_member(username, acctid, tel)
        assert username in addmember.get_memberlist()

