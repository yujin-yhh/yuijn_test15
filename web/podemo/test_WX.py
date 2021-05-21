from web.podemo.index_page import IndexPage


class TestWX:

    def setup(self):
        self.index = IndexPage()

    def test_registe(self):
        assert self.index.goto_register().register()