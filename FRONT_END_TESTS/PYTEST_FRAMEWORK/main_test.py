import pytest
import time
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from FRONT_END_TESTS.PYTEST_FRAMEWORK.locators import FirstPageLocators
from FRONT_END_TESTS.PYTEST_FRAMEWORK.wrappers import TestUtils as TU


def log_info(request, message):
    request.node.add_report_section("call", "log", f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")


@pytest.mark.usefixtures("request")
def test_food_menu(driver, request):
    driver.get("https://qaquickpay.hmshost.com/menu/112/208")

    try:
        TU.element_is_present(driver, FirstPageLocators.POP_UP_BUTTON).click()
        log_info(request, "Pop-up accepted")
    except TimeoutException:
        pass

    TU.element_is_present(driver, FirstPageLocators.SMASH_BURGER).click()

    smash_burger_text = TU.element_is_present(driver, FirstPageLocators.SMASH_BURGER_TITLE).text.replace('®', '')
    assert smash_burger_text == "Smash Burger", "Title is wrong"
    log_info(request, "Title test passed")

    TU.element_is_present(driver, FirstPageLocators.BACON_CHEESEBURGER).click()
    TU.move_to_element(driver, FirstPageLocators.MAYO).click()
    TU.move_to_element(driver, FirstPageLocators.LETTUCE).click()
    TU.move_to_element(driver, FirstPageLocators.CLASSIC_BUN).click()
    TU.move_to_element(driver, FirstPageLocators.DOUBLE_BEEF_PATTY).click()
    TU.move_to_element(driver, FirstPageLocators.BEEF_PATTY).click()

    TU.element_is_present(driver, FirstPageLocators.ADD_TO_CART).click()
    time.sleep(3)
    TU.move_to_element(driver, FirstPageLocators.GO_TO_CART).click()
    time.sleep(1)
    TU.move_to_element(driver, FirstPageLocators.PAY_NOW).click()
    time.sleep(3)
    TU.move_to_element(driver, FirstPageLocators.FIRST_NAME).send_keys(
        'test' + Keys.TAB + '4111 1111 1111 1111' + Keys.TAB + '08/25' + Keys.TAB + '123' + Keys.TAB + '1111')
    TU.move_to_element(driver, FirstPageLocators.PAY_BUTTON).click()
    time.sleep(5)

    TU.move_to_element(driver, FirstPageLocators.EMAIL_FIELD).send_keys('a.tevzadze100@gmail.com')
    TU.move_to_element(driver, FirstPageLocators.EMAIL_SEND_BUTTON).click()
    time.sleep(5)


if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
