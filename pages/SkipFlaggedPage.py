from pages.seleniumExtended import SeleniumExtended
from pages.locaters.SkipFlaggedLocators import SkipFlaggedLocators


class SkipFlagged(SkipFlaggedLocators):
    def __init__(self, driver) -> None:
        self.driver = driver
        self.sl = SeleniumExtended(driver)
        self.url = "https://skiplagged.com/"
        self.start()

    def start(self):
        self.driver.get(self.url)
        self.fill_countries()

    def fill_countries(self):
        print(self.LIST_OF_INPUTS)
        # self.sl.wait_and_input_text(self.LIST_OF_INPUTS[1], "TLV")
        # self.sl.wait_and_click(self.AUTO_COMPLETE)
        # self.sl.wait_and_input_text(self.LIST_OF_INPUTS[1], "BER")
