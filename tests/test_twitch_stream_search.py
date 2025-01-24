def test_twitch_stream_search(twitch_main_page):
    twitch_main_page.accept_cookies()
    twitch_main_page.click_browse()
    twitch_main_page.search_game("StarCraft II")
    twitch_main_page.scroll_down(2)
    twitch_main_page.select_random_video()
    twitch_main_page.wait_for_video_and_screenshot("streamer_page_screenshot.png")
