from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AboutPage(BasePage):

    ONLINE = (By.XPATH, '//*[@id="about_greeting"]/div[3]/div[1]')
    PLAYING = (By.XPATH, '//*[@id="about_greeting"]/div[3]/div[2]')
    STORE_LINK = (By.XPATH, '//a[contains(text(), "STORE")]')

    def __init__(self, driver):
        super().__init__(driver)

    def do_get_online(self):
        return int("".join(self.do_get_element_text(self.ONLINE).split('\n')[1].split(',')))

    def do_get_playing(self):
        return int("".join(self.do_get_element_text(self.PLAYING).split('\n')[1].split(',')))
