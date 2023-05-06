from selenium.webdriver.common.by import By


class SkyScannerLocators:
    FROM = (By.ID, "originInput-input")
    TO = (By.ID, "destinationInput-input")
    ORIGIN_POPUP = (By.ID, "#originInput-menu")
    DESTINATION_POPUP = (By.ID, "#destinationInput-menu")
    SEARCH = (By.CSS_SELECTOR, "button.SearchControls_desktopCTA__MDIxY")
    SORT = (By.CSS_SELECTOR, "select.BpkSelect_bpk-select__OTkyN")
