from pages.seleniumExtended import SeleniumExtended
from pages.locaters.SkyScannerLocators import SkyScannerLocators


class SkyScanner(SkyScannerLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)
        self.url = "https:/skyscanner.co.il/"
        self.start()

    def start(self):
        self.driver.get(self.url)

    def fill_countries(self, origin, destination):
        # handle the origin
        self.driver.find_element(self.TO).clear()
        self.sl.wait_and_input_text(self.FROM, origin)
        self.sl.wait_until_element_is_clickble(self.ORIGIN_POPUP[0])

        # handle the destination
        self.sl.wait_and_input_text(self.TO, destination)
        self.sl.wait_until_element_is_clickble(self.DESTINATION_POPUP[0])

        # click on the searchbox
        self.sl.wait_until_element_is_clickble(self.SEARCH)

        # verify it did search
        self.sl.wait_until_element_is_clickble(self.SORT)
        url = self.driver.current_url
        return url
