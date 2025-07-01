import pytest
import allure
from selene import browser
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
import os
from utils.attach import add_screenshot, add_logs, add_html, add_video


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.set_capability('selenoid:options', selenoid_capabilities)

    browser.config.driver = Remote(
        command_executor=f"https://{os.getenv('LOGIN')}:{os.getenv('PASSWORD')}@{os.getenv('REMOTE_URL')}/wd/hub",
        options=options
    )

    browser.config.base_url = os.getenv('ROOT_URL')
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10

    yield

    add_screenshot(browser)
    add_html(browser)
    add_logs(browser)
    add_video(browser)

    browser.quit()