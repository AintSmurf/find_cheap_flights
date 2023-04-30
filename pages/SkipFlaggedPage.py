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

    def fill_countries(self, origin, destination):
        # get all elements to send keys
        elements = self.sl.wait_and_get_elements(self.LIST_OF_INPUTS)

        # first box
        elements[0].clear()
        elements[0].send_keys(origin)
        self.sl.wait_until_element_is_clickble(self.AUTO_COMPLETE_FIRST)

        # second box
        elements[1].send_keys(destination)
        self.sl.wait_until_element_is_clickble(self.AUTO_COMPLETE_SECOND)

        # change trip type
        self.sl.wait_and_click(self.TRIP_TYPE)
        self.sl.wait_until_element_is_clickble(self.ONE_WAY)

        # search
        self.sl.wait_and_click(self.SEARCH_BUTTON)

        # return the url
        url = self.driver.current_url
        self.driver.quit()
        return url
