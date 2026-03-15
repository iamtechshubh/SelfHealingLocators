from framework.driver_setup import get_driver
from framework.healer import find_element

def test_login():

    driver = get_driver()

    driver.get("https://www.saucedemo.com")

    username = find_element(driver, "username")
    password = find_element(driver, "password")
    login = find_element(driver, "login_button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login.click()