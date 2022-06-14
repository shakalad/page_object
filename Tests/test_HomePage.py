import time

from Tests.test_base import BaseTest
from Pages.HomePage import HomePage
from Pages.AboutPage import AboutPage
from Pages.TopSellersPage import TopSellersPage
from Pages.FirstGamePage import FirstGamePage
from Config.config import TestData


class Test_HomePage(BaseTest):

    # def test_case_one(self):
    #     self.homePage = HomePage(self.driver)
    #     title = self.homePage.do_get_title("Welcome to Steam")
    #     assert title == TestData.home_page_title, "Main page is not opened!"
    #
    #     self.homePage.do_click(self.homePage.ABOUT_LINK)
    #
    #     self.aboutPage = AboutPage(self.driver)
    #     title = self.aboutPage.do_get_title("Steam, The Ultimate Online Game Platform")
    #     assert title == TestData.about_page_title, "Error About page is not opened!"
    #
    #     online = self.aboutPage.do_get_online()
    #     playing = self.aboutPage.do_get_playing()
    #     assert online > playing, "Error online players are less than playing"
    #
    #     self.aboutPage.do_click(self.aboutPage.STORE_LINK)
    #
    #     assert self.homePage.do_get_title("Welcome to Steam") == TestData.home_page_title, "Main page is not opened!"

    def test_case_two(self):
        self.homePage = HomePage(self.driver)
        assert self.homePage.do_get_title("Welcome to Steam") == TestData.home_page_title, "Main page is not opened!"

        self.homePage.go_to_top_sellers()

        self.topSellersPage = TopSellersPage(self.driver)
        title = self.topSellersPage.get_h2_title()
        assert title == TestData.top_sellers_title, "Error top sellers page is not opened!"

        self.topSellersPage.do_click_checkboxes()
        search_result = self.topSellersPage.get_search_result()
        actual = self.topSellersPage.get_results_actual()
        # assert search_result == actual, "Error results doesn't match"

        first_games_name = self.topSellersPage.get_first_games_name()
        first_games_release = self.topSellersPage.get_first_games_release_date()
        first_games_price = self.topSellersPage.get_first_games_price()

        self.topSellersPage.do_click_on_first_game()

        self.FirstGamePage = FirstGamePage(self.driver)
        game_name = self.FirstGamePage.get_game_name()
        print(game_name)
        game_release = self.FirstGamePage.get_game_release()
        game_price = self.FirstGamePage.get_game_price()
        game_description = self.FirstGamePage.get_game_description()
        assert game_description == TestData.first_game_description, "Error descriptions doesn't match!"
        assert first_games_name == game_name, f"Error game names doesn't match!"
        assert first_games_release == game_release, "Error release dates doesn't match!"
        assert first_games_price == game_price, f"Error prices doesn't match! {first_games_price} and {game_price}"
