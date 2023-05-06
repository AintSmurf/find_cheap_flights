from pages.seleniumExtended import SeleniumExtended
from selenium.webdriver.chrome.options import Options
from pages.locaters.SkyScannerLocators import SkyScannerLocators


class SkyScanner(SkyScannerLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)
        self.url = "https://www.skyscanner.co.il/"
        self.start()

    def start(self):
        self.driver.get(self.url)

    def fill_countries(self, origin, destination):
        # handle the origin
        self.sl.wait_and_input_text(self.FROM, origin)
        self.sl.wait_and_click(self.ORIGIN_POPUP[0])

        # handle the destination
        self.sl.wait_and_input_text(self.TO, destination)
        self.sl.wait_and_click(self.DESTINATION_POPUP[0])

        # click on the searchbox
        self.sl.wait_and_click(self.SEARCH)

        # verify it did search
        self.sl.wait_until_element_is_clickble(self.SORT)
        url = self.driver.current_url
        return url
