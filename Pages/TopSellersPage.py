import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData


class TopSellersPage(BasePage):
    TOP_SELLERS_H2 = (By.XPATH, "//h2[contains(text(),'Top Sellers')]")
    ACTION = (By.XPATH, "//div[@data-loc='Action']")
    NARROW = (By.XPATH, "//div[contains(text(), 'Narrow by number of players')]")
    LAN_COOP = (By.XPATH, "//span[contains(text(), 'LAN Co-op')]")
    STEAM_LINUX = (By.XPATH, "//span[contains(text(), 'SteamOS + Linux')]")
    CHECKED = (By.XPATH, "//div[contains(@class, 'checked')]")
    SEARCH_RESULT = (By.XPATH, "//div[contains(@class, 'search_results_count')]")
    GAMES_FOUND = (By.XPATH, "//a[contains(@class, 'search_result_row')]")
    FIRST_GAME_IN_LIST = (By.XPATH, "//a[contains(@class, 'search_result_row')][1]")
    FIRST_GAMES_NAME = (By.XPATH, '//*[@id="search_resultsRows"]/a[1]/div[2]/div[1]/span')
    FIRST_GAMES_RELEASE_DATE = (By.XPATH, '//*[@id="search_resultsRows"]/a[1]/div[2]/div[2]')
    FIRST_GAMES_PRICE = (By.XPATH, '//*[@id="search_resultsRows"]/a[1]/div[2]/div[4]/div[2]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_h2_title(self):
        return self.do_get_element_text(self.TOP_SELLERS_H2)

    def do_click_checkboxes(self):
        self.do_click(self.ACTION)
        self.do_click(self.NARROW)
        time.sleep(2)
        self.do_click(self.LAN_COOP)
        self.do_click(self.STEAM_LINUX)

    def get_search_result(self):
        self.is_text_loaded(self.SEARCH_RESULT, TestData.expected_game_quantity)
        return int(self.do_get_element_text(self.SEARCH_RESULT).split(" ")[0])

    def get_results_actual(self):
        return len(self.driver.find_elements(By.XPATH, "//a[contains(@class, 'search_result_row')]"))

    def get_first_games_name(self):
        return self.do_get_element_text(self.FIRST_GAMES_NAME)

    def get_first_games_release_date(self):
        return self.do_get_element_text(self.FIRST_GAMES_RELEASE_DATE)

    def get_first_games_price(self):
        return self.do_get_element_text(self.FIRST_GAMES_PRICE)

    def do_click_on_first_game(self):
        self.do_click(self.FIRST_GAME_IN_LIST)
