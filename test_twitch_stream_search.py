import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_twitch_stream_search(driver):
    # 1. Go to Twitch mobile site
    driver.get("https://m.twitch.tv/")
    time.sleep(3)

    # 1.1 Accept Cookies if the banner appears
    try:
        cookie_banner_accept = driver.find_element(By.XPATH, "//div[text()='Accept']")
        cookie_banner_accept.click()
        time.sleep(2)
    except:
        print("No cookie banner found, proceeding...")

    # 2. Click on the search icon
    search_icon = driver.find_element(By.XPATH, "//div[text()='Browse']")
    search_icon.click()
    time.sleep(2)

    # 3. Input "StarCraft II"
    search_input = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_input.send_keys("StarCraft II")
    search_input.send_keys(Keys.ENTER)
    time.sleep(3)

    # 4. Scroll down 2 times
    actions = ActionChains(driver)
    for _ in range(2):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)

    # 5. Select a random streamer
    main_content = driver.find_element(By.ID, "page-main-content-wrapper")
    last_section = main_content.find_element(By.XPATH, "./div/div/section[last()]")
    random_video_div = last_section.find_element(By.XPATH, f"./div[{random.randint(2, 3)}]")
    random_video_div.click()

    # 6. Wait for the streamer's page to load completely and take a screenshot
    time.sleep(10)
    driver.save_screenshot("streamer_page_screenshot.png")
    print("Screenshot saved as 'streamer_page_screenshot.png'")
