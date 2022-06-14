from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from Pages.BasePage import BasePage
from Config.config import TestData


class HomePage(BasePage):

    ABOUT_LINK = (By.XPATH, "//a[contains(text(), 'ABOUT')]")
    NEW_AND_NOTEWORTHY = (By.ID, 'noteworthy_tab')
    COMMUNITY = (By.XPATH, "//a[contains(text(), 'COMMUNITY')]")
    TOP_SELLERS_LINK = (By.XPATH, "//a[contains(text(),'Top Sellers')]")
    MARKET_LINK = (By.XPATH, '//*[@id="global_header"]/div/div[2]/div[2]/div/a[4]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.home_page)

    def go_to_top_sellers(self):
        action = ActionChains(self.driver)
        menu = self.do_get_element(self.NEW_AND_NOTEWORTHY)
        action.move_to_element(menu).perform()
        self.do_click(self.TOP_SELLERS_LINK)

    def go_to_market(self):
        action = ActionChains(self.driver)
        menu = self.do_get_element(self.COMMUNITY)
        action.move_to_element(menu).perform()
        self.do_click(self.MARKET_LINK)
