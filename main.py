from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.SkyScannerPage import SkyScanner
from pages.SkipFlaggedPage import SkipFlagged
from helpers.MakeItCsv import CovertToCSV
from helpers.delete import System_helper
import threading


def get_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    return driver


def start_search(flight_class, driver):
    flight_object = flight_class(driver)
    url = flight_object.fill_countries("TLV", "BERLIN")
    return url


def main():
    excel = CovertToCSV()
    system_helper = System_helper()
    list_of_url = []
    list_of_classes = [SkipFlagged, SkyScanner]
    driver = get_driver()

    threads = []
    for flight_class in list_of_classes:
        thread = threading.Thread(target=start_search, args=(flight_class, driver))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        url = thread.result()
        list_of_url.append(url)

    driver.quit()

    excel.convert(list_of_url)
    excel.convert_to_excel()

    system_helper.delete_file()


if __name__ == "__main__":
    main()
