from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from framework.healer import find_element


def safe_find(driver, locator):

    by = locator["by"]
    value = locator["value"]

    try:
        element = driver.find_element(getattr(By, by.upper()), value)
        print("Locator found normally")
        return element

    except NoSuchElementException:

        print("Locator failed, trying healing...")

        healed_element = find_element(driver, value)

        if healed_element:
            print("Healing successful")
            return healed_element

        else:
            raise Exception("Element not found even after healing")