from Tests.test_base import BaseTest
from Pages.HomePage import HomePage
from Pages.AboutPage import AboutPage


class Test_HomePage(BaseTest):

    def test_case_one(self):
        self.page = HomePage(self.driver)
        title = self.page.do_get_title("Welcome to Steam")
        assert title == "Welcome to Steam", "Main page is not opened!"

        self.page.do_click(self.page.ABOUT_LINK)
        self.page = AboutPage(self.driver)
        title = self.page.do_get_title("Steam, The Ultimate Online Game Platform")
        assert title == "Steam, The Ultimate Online Game Platform"

        online = self.page.do_get_online()
        playing = self.page.do_get_playing()
        assert online > playing, "Error online players are less than playing"

        self.page.do_click(self.page.STORE_LINK)
        assert self.page.do_get_title("Welcome to Steam") == "Welcome to Steam", "Main page is not opened !"

