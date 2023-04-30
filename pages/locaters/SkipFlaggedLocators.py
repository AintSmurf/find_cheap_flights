from selenium.webdriver.common.by import By


class SkipFlaggedLocators:
    TRIP_TYPE = (
        By.XPATH,
        "/html/body/div[1]/div/main/div[1]/form/div[1]/div[1]/button/span",
    )
    ONE_WAY = (By.CSS_SELECTOR, 'div[data-trip-type="one-way"]')
    AUTO_COMPLETE_FIRST = (
        By.XPATH,
        "/html/body/div[1]/div/main/div[1]/form/ul[1]/li/a/span[1]",
    )
    AUTO_COMPLETE_SECOND = (
        By.XPATH,
        "/html/body/div[1]/div/main/div[1]/form/ul[2]/li[1]/a/span[1]",
    )
    LIST_OF_INPUTS = (By.CSS_SELECTOR, "input[type='text']")
    SEARCH_BUTTON = (By.XPATH, '//*[@id="home-container"]/div[1]/form/div[2]/button')
