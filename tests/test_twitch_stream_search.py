import allure
import pytest


@allure.suite("Twitch Stream Search")
class TestTwitchStreamSearch:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Check the basic functionality of the twitch search")
    @pytest.mark.parametrize("game_name", ["StarCraft II"])
    def test_twitch_stream_search(self, twitch_main_page, game_name):
        with allure.step("Accept Cookies if the banner appears"):
            twitch_main_page.accept_cookies()

        with allure.step("Click on the search icon"):
            twitch_main_page.click_browse()

        with allure.step(f"Input '{game_name}'"):
            twitch_main_page.search_game(game_name)

        with allure.step("Scroll down 2 times"):
            twitch_main_page.scroll_down(2)

        with allure.step("Select a random streamer"):
            twitch_main_page.select_random_video()

        with allure.step("Wait for the streamer's page to load completely and take a screenshot"):
            twitch_main_page.wait_for_video_and_screenshot(f"{game_name} streamer page screenshot.png")
