from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Utils.UtilsFile import CHROME_DRIVER_FILE_PATH


def init_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_FILE_PATH, chrome_options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    return driver


def find_element(by, value, driver):
    element = None
    try:
        element = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((by, value))
        )
    except NoSuchElementException:
        print("Could not find element by given locator")
    finally:
        return element


def get_element_text(by, value, driver):
    return find_element(by, value, driver).text

