from snowball.pages.mainpage import MainPage


class TestSearch:

    # def setup_class(self):
    #     self.main = MainPage()

    def test_search(self):
        MainPage().goto_main().goto_market().goto_search().search()
