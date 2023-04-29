from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.SkyScannerPage import SkyScanner
from selenium.webdriver.common.by import By
from pages.SkipFlaggedPage import SkipFlagged


def get_driver():
    # objects
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
    return driver


def main():
    driver = get_driver()
    SkipFlagged(driver)
    # driver.get("https://skiplagged.com/")
    # list_of_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    # list_of_inputs[0].clear()
    # list_of_inputs[0].send_keys("TLV")
    # driver.find_element(By.CLASS_NAME, "autocomplete-title")
    # list_of_inputs[1].send_keys("BER")
    # driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")[0].click()


main()
