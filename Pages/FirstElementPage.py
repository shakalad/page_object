from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class FirstElementPage(BasePage):

    INFO_DIV = (By.XPATH, '//div[@id="largeiteminfo_content"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_text(self):
        return self.do_get_element_text(self.INFO_DIV)
