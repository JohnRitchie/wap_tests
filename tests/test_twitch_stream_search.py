import allure


@allure.suite("Twitch Stream Ssearch")
class TestTwitchStreamSsearch:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Check the basic functionality of the twitch search")
    def test_twitch_stream_search(self, twitch_main_page):
        with allure.step("Accept Cookies if the banner appears"):
            twitch_main_page.accept_cookies()

        with allure.step("Click on the search icon"):
            twitch_main_page.click_browse()

        with allure.step("Input 'StarCraft II'"):
            twitch_main_page.search_game("StarCraft II")

        with allure.step("Scroll down 2 times"):
            twitch_main_page.scroll_down(2)

        with allure.step("Select a random streamer"):
            twitch_main_page.select_random_video()

        with allure.step("Wait for the streamer's page to load completely and take a screenshot"):
            twitch_main_page.wait_for_video_and_screenshot("streamer_page_screenshot.png")
