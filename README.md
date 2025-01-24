# Twitch Stream Search Testing Project

## Overview
This project automates the testing of the Twitch mobile website's search functionality. The main objective is to ensure that users can:

1. Navigate to the Twitch mobile website.
2. Search for a specific game (e.g., "StarCraft II").
3. Scroll through the results.
4. Select and open a random stream video from the results.
5. Verify the video is successfully loaded by capturing a screenshot and embedding it in an Allure report.

## Project Structure

```
.
├── requirements.txt
├── pages/
│   └── twitch_main_page.py
├── tests/
│   ├── conftest.py
│   └── test_twitch_stream_search.py
└── README.md
```

### Files and Directories

- **requirements.txt**: Contains the necessary dependencies for the project.
- **pages/**: Includes the `TwitchMainPage` class, implementing the Page Object Model (POM) for interaction with the Twitch mobile website.
- **tests/**:
  - `conftest.py`: Defines fixtures for setting up the Selenium WebDriver and initializing the page object.
  - `test_twitch_stream_search.py`: Contains the main test case using Pytest and Allure.
- **README.md**: This documentation.

## Prerequisites

Before running the tests, ensure you have the following installed:

- Python 3.10+
- pip (Python package manager)

## Setup

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Tests

1. Execute the tests with Pytest:
   ```bash
   pytest --alluredir=allure-results
   ```

2. To generate and view the Allure report:
   ```bash
   allure serve allure-results
   ```

## Key Features

- **Page Object Model (POM)**: Encapsulation of web page interactions in the `TwitchMainPage` class for better maintainability.
- **Allure Reporting**: Steps and screenshots are embedded in the test report for clear insights into the test execution.
- **Randomized Video Selection**: Tests include randomization to verify robustness across different content scenarios.
- **Mobile Emulation**: The tests are designed to run on an emulated mobile browser (iPhone X).

## Implementation Details

### TwitchMainPage Class
This class encapsulates the main actions performed on the Twitch mobile website:

- `navigate()`: Opens the Twitch mobile website.
- `accept_cookies()`: Handles the cookie banner (if present).
- `click_browse()`: Clicks on the "Browse" option.
- `search_game(game_name)`: Inputs the specified game name into the search field.
- `scroll_down(times)`: Scrolls down the page a specified number of times.
- `select_random_video()`: Selects a random video from the last section of the page.
- `wait_for_video_and_screenshot(screenshot_name)`: Waits for a video to load and captures a screenshot, attaching it to the Allure report.

### Test Case
The `test_twitch_stream_search` test performs the following steps:

1. Navigates to the Twitch mobile site.
2. Accepts cookies if prompted.
3. Searches for the game "StarCraft II".
4. Scrolls down to the video section.
5. Selects a random stream video and opens it.
6. Waits for the video to load and captures a screenshot.

### Fixtures

- `driver`: Initializes the Selenium WebDriver with Chrome mobile emulation (iPhone X).
- `twitch_main_page`: Initializes the `TwitchMainPage` object and navigates to the Twitch mobile site.

## Example Output

When the test runs successfully, you can find the following in the Allure report:

- **Step-by-step execution**: Each step of the test is logged.
- **Screenshots**: A screenshot of the video page is embedded in the report.

## Dependencies

The project uses the following libraries:

- `pytest`: Test framework.
- `selenium`: Browser automation library.
- `allure-pytest`: Integration with Allure for enhanced reporting.
- `webdriver_manager`: Simplifies the setup of WebDriver binaries.

## Known Limitations

- The test is designed for the Twitch mobile website and may not work on the desktop version.
- Random video selection assumes the presence of at least two videos in the last section.
- Network or site changes may require updates to locators or other logic.

## Contribution

Feel free to submit issues or pull requests to improve this project. Contributions are welcome!
