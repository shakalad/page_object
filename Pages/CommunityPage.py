import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Config.config import TestData
from Pages.BasePage import BasePage


class CommunityPage(BasePage):

    PAGE_HEADER = (By.XPATH, "//span[contains(text(), 'Community Market')]")
    TITLE_TEXT = (By.XPATH, "//div[@class='newmodal'][6]//div[@class='title_text']")
    ADVANCED_OPTIONS = (By.XPATH, "//div[@id='market_search_advanced_show']")
    ALL_GAMES = (By.XPATH, "//div[@id='app_option_0_selected']")
    DOTA_2 = (By.XPATH, "//div[@id='market_advancedsearch_appselect_options_apps']//span[contains(text(), 'Dota 2')]")
    SELECT_ANY = (By.XPATH, "//select[@name='category_570_Hero[]']")
    IMMORTAL = (By.ID, 'tag_570_Rarity_Rarity_Immortal')
    SEARCH_FIELD = (By.ID, 'advancedSearchBox')
    SEARCH_BUTTON = (By.XPATH, "//div[@class='btn_medium btn_green_white_innerfade']")
    SEARCH_FILTERS = (By.XPATH, "//a[@class='market_searchedForTerm']")
    SEARCH_RESULTS = (By.ID, 'searchResultsRows')
    DOTA_FILTER_CLOSE = (By.XPATH, '//*[@id="BG_bottom"]/div[1]/div/a[1]')
    GOLDEN_FILTER_CLOSE = (By.XPATH, '//*[@id="BG_bottom"]/div[1]/div/a[4]')
    FIRST_ELEMENT = (By.ID, 'resultlink_0')

    def __init__(self, driver):
        super().__init__(driver)

    def get_modal_title(self):
        return self.do_get_element_text(self.TITLE_TEXT)

    def do_add_filters(self):
        self.do_click(self.ADVANCED_OPTIONS)
        self.do_click(self.ALL_GAMES)
        self.do_click(self.DOTA_2)
        select = Select(self.do_get_element(self.SELECT_ANY))
        select.select_by_value(TestData.filter_character_value)
        self.do_click(self.IMMORTAL)
        self.do_send_keys(self.SEARCH_FIELD, TestData.filter_search)
        self.do_click(self.SEARCH_BUTTON)

    def do_get_filters(self):
        filters = self.driver.find_elements(By.XPATH, "//a[@class='market_searchedForTerm']")
        filter_names = [(element.text).strip('"') for element in filters]
        return filter_names

    def do_get_first_five_results(self):
        parent = self.do_get_element(self.SEARCH_RESULTS)
        hrefs = parent.find_elements(By.TAG_NAME, "a")
        return hrefs[0:5]

    def do_delete_filters(self):
        self.do_click(self.DOTA_FILTER_CLOSE)
        self.do_click(self.GOLDEN_FILTER_CLOSE)

    def click_on_first_element(self):
        self.do_click(self.FIRST_ELEMENT)

