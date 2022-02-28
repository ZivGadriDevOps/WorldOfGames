from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

BAD_RETURN_CODE = -1
GOOD_RETURN_CODE = 0
IS_USER_EXIST = False
CHROME_DRIVER_FILE_PATH = "../Utils/chromedriver.exe"


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
        element = driver.find_element(by, value)
    except NoSuchElementException:
        print("Could not find element by given locator")
        exit(-1)
    finally:
        return element


def get_element_text(by, value, driver):
    return find_element(by, value, driver).text


def test_scores_service(url):
    driver = init_driver()
    try:
        driver.get(url)
        sleep(3)
        score_raw = get_element_text(By.XPATH, "//div[@class='container text-center']//strong/div", driver)
        score = score_raw.split(" ")[0]
        driver.quit()
        if 1 <= int(score) <= 1000:
            print(f"Test passed! Score {score} is between 1 and 1000")
            return True
        else:
            print(f"Test failed! Score {score} is not between 1 and 1000")
            return False
    except WebDriverException:
        print("Could not load the page.")
        exit(-1)


def main_function(url):
    try:
        if test_scores_service(url):
            exit(GOOD_RETURN_CODE)
        else:
            exit(BAD_RETURN_CODE)
    except WebDriverException:
        exit(-1)
