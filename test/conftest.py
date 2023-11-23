from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = 'https://app.qa.guru/automation-practice-form/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()