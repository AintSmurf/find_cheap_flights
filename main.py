from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.SkyScannerPage import SkyScanner
from pages.SkipFlaggedPage import SkipFlagged
from helpers.MakeItCsv import CovertToCSV
from helpers.delete import System_helper


def get_driver():
    # objects
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    return driver


def main():
    # objects
    excel = CovertToCSV()
    system_helper = System_helper()
    list_of_url = []

    driver = get_driver()
    sf = SkipFlagged(driver)
    url = sf.fill_countries("TLV", "BERLIN")
    list_of_url.append([sf.__class__.__name__, url])

    driver = get_driver()
    sk = SkyScanner(driver)
    url = sk.fill_countries("TLV", "BERLIN")
    list_of_url.append([sk.__class__.__name__, url])

    excel.convert(list_of_url)
    excel.convert_to_excel()

    system_helper.delete_file()


main()
