import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_twitch_stream_search(driver):
    # 1. Go to Twitch mobile site
    driver.get("https://m.twitch.tv/")
    time.sleep(3)

    # 1.1 Accept Cookies if the banner appears
    try:
        cookie_banner_accept = driver.find_element(By.XPATH, "//div[text()='Принять']") #todo:
        cookie_banner_accept.click()
        time.sleep(2)
    except:
        print("No cookie banner found, proceeding...")

    # 2. Click on the search icon
    search_icon = driver.find_element(By.CSS_SELECTOR, "button[data-a-target='search-input-trigger']")
    search_icon.click()
    time.sleep(2)

    # 3. Input "StarCraft II"
    search_input = driver.find_element(By.CSS_SELECTOR, "input[data-a-target='search-input']")
    search_input.send_keys("StarCraft II")
    search_input.send_keys(Keys.ENTER)
    time.sleep(3)

    # 4. Scroll down 2 times
    actions = ActionChains(driver)
    for _ in range(2):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    # 5. Select a streamer
    streamer = driver.find_element(By.CSS_SELECTOR, "a[data-a-target='preview-card-title-link']")
    streamer.click()
    time.sleep(5)

    # 6. Wait for the streamer's page to load completely and take a screenshot
    time.sleep(10)
    driver.save_screenshot("streamer_page_screenshot.png")
    print("Screenshot saved as 'streamer_page_screenshot.png'")
