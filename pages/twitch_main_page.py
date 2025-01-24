import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TwitchMainPage:
    def __init__(self, driver):
        self.url = "https://m.twitch.tv/"
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def navigate(self):
        self.driver.get(self.url)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def accept_cookies(self):
        try:
            cookie_banner_accept = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Accept']"))
            )
            cookie_banner_accept.click()
        except:
            print("No cookie banner found, proceeding...")

    def click_browse(self):
        search_icon = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Browse']"))
        )
        search_icon.click()

    def search_game(self, game_name):
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
        )
        search_input.send_keys(game_name)
        search_input.send_keys(Keys.ENTER)

    def scroll_down(self, times=2):
        for _ in range(times):
            self.actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(2)

    def select_random_video(self):
        main_content = self.wait.until(
            EC.presence_of_element_located((By.ID, "page-main-content-wrapper"))
        )
        last_section = main_content.find_element(By.XPATH, "./div/div/section[last()]")
        random_video_div = last_section.find_element(By.XPATH, f"./div[{random.randint(2, 3)}]")
        random_video_div.click()

    def wait_for_video_and_screenshot(self, screenshot_name):
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "video"))
        )
        self.driver.save_screenshot(screenshot_name)
