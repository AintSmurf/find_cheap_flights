from selenium.webdriver.common.by import By


class SkyScannerLocators:
    FROM = (By.ID, "originInput-input")
    TO = (By.ID, "destinationInput-input")
    SEARCH = (By.XPATH, '//*[@id="app-root"]/div[1]/div/main/div[1]/div/div/div/button')
