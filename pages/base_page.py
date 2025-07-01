import allure
from selene import browser, have
import os

class BasePage:
    @allure.step("Открыть страницу")
    def open(self, url=None):
        target_url = url or os.getenv('ROOT_URL')
        browser.open(target_url)