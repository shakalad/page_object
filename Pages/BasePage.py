from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()
        field.send_keys(text)

    def do_get_element_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        return bool(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)))

    def do_get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def do_get_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def is_text_loaded(self, locator, text):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))

    def do_get_all_elements(self, locator):
        return self.driver.find_elements(locator)
