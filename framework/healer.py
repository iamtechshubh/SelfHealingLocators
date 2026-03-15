import json
import difflib
from selenium.common.exceptions import NoSuchElementException


def load_locators():
    with open("locator_store.json") as f:
        return json.load(f)


def find_element(driver, key):

    locators = load_locators()
    locator = locators[key]

    by = locator["by"]
    value = locator["value"]

    try:
        return driver.find_element(by, value)

    except NoSuchElementException:

        print(f"Locator {value} failed. Healing started...")

        page = driver.page_source

        # collect possible ids from DOM
        import re
        ids = re.findall(r'id="([^"]+)"', page)

        # find closest match
        match = difflib.get_close_matches(value, ids, n=1)

        if match:
            healed = match[0]
            print(f"Healed locator found: {healed}")

            return driver.find_element("id", healed)

        raise
