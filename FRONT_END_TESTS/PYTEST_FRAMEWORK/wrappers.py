from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestUtils:
    @staticmethod
    def open(driver, url):
        driver.get(url)

    @staticmethod
    def element_is_visible(driver, locator, timeout=10):
        return wait(driver, timeout).until(EC.visibility_of_element_located(locator))

    @staticmethod
    def elements_are_visible(driver, locator, timeout=10):
        return wait(driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @staticmethod
    def element_is_present(driver, locator, timeout=10):
        time.sleep(0.5)
        return wait(driver, timeout).until(EC.presence_of_element_located(locator))

    @staticmethod
    def elements_are_present(driver, locator, timeout=10):
        return wait(driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @staticmethod
    def element_is_clickable(driver, locator, timeout=10):
        return wait(driver, timeout).until(EC.element_to_be_clickable(locator))

    @staticmethod
    def element_is_not_visible(driver, locator, timeout=10):
        return wait(driver, timeout).until(EC.invisibility_of_element(locator))

    @staticmethod
    def scroll_to_bottom(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @staticmethod
    def double_click(driver, locator, timeout=10):
        element = wait(driver, timeout).until(EC.presence_of_element_located(locator))
        actions = ActionChains(driver)
        actions.double_click(element).perform()

    @staticmethod
    def right_click(driver, locator, timeout=10):
        element = wait(driver, timeout).until(EC.presence_of_element_located(locator))
        actions = ActionChains(driver)
        actions.context_click(element).perform()

    @staticmethod
    def click_and_hold(driver, locator, timeout=10):
        element = wait(driver, timeout).until(EC.presence_of_element_located(locator))
        actions = ActionChains(driver)
        actions.click_and_hold(element).perform()

    @staticmethod
    def drag_and_drop(driver, locator, target_locator, timeout=10):
        element = wait(driver, timeout).until(EC.presence_of_element_located(locator))
        target_element = wait(driver, timeout).until(EC.presence_of_element_located(target_locator))
        actions = ActionChains(driver)
        actions.drag_and_drop(element, target_element).perform()

    @staticmethod
    def click(driver, locator, timeout=10):
        element = wait(driver, timeout).until(EC.presence_of_element_located(locator))
        actions = ActionChains(driver)
        actions.click(element).perform()

    @staticmethod
    def go_to_element(driver, locator, timeout=10):
        element = wait(driver, timeout).until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @staticmethod
    def move_to_element(driver, locator, timeout=10):
        element = wait(driver, timeout).until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        return element

    @staticmethod
    def move_and_click(driver, locator, timeout=10):
        element = wait(driver, timeout).until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        return element

    @staticmethod
    def scroll_slowly_to_bottom(driver, scroll_pause_time=1):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    @staticmethod
    def scroll_slowly_by_pixel(driver, total_height=None, step=5, pause_time=3):
        if total_height is None:
            total_height = driver.execute_script("return document.body.scrollHeight")
        current_position = 0
        while current_position < total_height:
            driver.execute_script(f"window.scrollTo(0, {current_position});")
            current_position += step
            time.sleep(pause_time)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


