from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class FirstGamePage(BasePage):

    GAME_NAME = (By.XPATH, "//div[@id='appHubAppName']")
    GAME_RELEASE_DATE = (By.XPATH, "//div[@class='date']")
    GAME_PRICE = (By.XPATH, "//div[@class='game_purchase_price price']")
    GAME_DESCRIPTION = (By.XPATH, "//div[@class='game_description_snippet']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_game_name(self):
        return self.do_get_element_text(self.GAME_NAME)

    def get_game_release(self):
        return self.do_get_element_text(self.GAME_RELEASE_DATE)

    def get_game_price(self):
        return self.do_get_element_text(self.GAME_PRICE).strip().split(" ")[0]

    def get_game_description(self):
        return self.do_get_element_text(self.GAME_DESCRIPTION)
