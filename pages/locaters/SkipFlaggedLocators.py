from selenium.webdriver.common.by import By


class SkipFlaggedLocators:
    AUTO_COMPLETE = (
        By.XPATH,
        "/html/body/div[1]/div/main/div[1]/form/ul[1]/li[1]",
    )
    LIST_OF_INPUTS = (By.CSS_SELECTOR, "input[type='text']")
