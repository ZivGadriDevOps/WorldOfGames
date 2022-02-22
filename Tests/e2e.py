from selenium.webdriver.common.by import By
from Utils.UtilsFile import APP_URL, BAD_RETURN_CODE, GOOD_RETURN_CODE

from TestHelper import get_element_text, init_driver


def test_scores_service(url):
    driver = init_driver()
    driver.get(url)
    score_raw = get_element_text(By.XPATH, "//div[@class='container text-center']//strong/div", driver)
    score = score_raw.split(" ")[0]
    if 1 <= score <= 1000:
        return True
    else:
        return False


def main_function():
    if test_scores_service(APP_URL):
        exit(GOOD_RETURN_CODE)
    else:
        exit(BAD_RETURN_CODE)
