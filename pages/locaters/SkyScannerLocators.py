from selenium.webdriver.common.by import By


class SkyScannerLocators:
    FROM = (By.ID, "originInput-input")
    TO = (By.ID, "destinationInput-input")
    SEARCH = (By.CSS_SELECTOR, "button.BpkButtonBase_bpk-button__NmRiZ")
    SORT = (By.CSS_SELECTOR, "select.BpkSelect_bpk-select__OTkyN")
