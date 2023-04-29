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
        self.fill_countries()

    def fill_countries(self):
        self.sl.wait_and_input_text(self.FROM, "TLV")
        self.sl.wait_and_input_text(self.TO, "BER")
        self.sl.wait_and_click(self.SEARCH)
