import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.twitch_main_page import TwitchMainPage


@pytest.fixture(scope="module")
def driver():
    print("\nstart driver")
    mobile_emulation = {"deviceName": "iPhone X"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--lang=en-US")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver

    print("\nquit driver")
    driver.quit()

@pytest.fixture(scope="function")
def twitch_main_page(driver):
    with allure.step("Go to Twitch mobile site"):
        page_obj = TwitchMainPage(driver)
        page_obj.navigate()

    return page_obj
