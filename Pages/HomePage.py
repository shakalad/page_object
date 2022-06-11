from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData


class HomePage(BasePage):

    ABOUT_LINK = (By.XPATH, "//a[contains(text(), 'ABOUT')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Home_page)

