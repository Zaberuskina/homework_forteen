import allure
from selene import browser, have
from locators.header_locators import HeaderLocators
import os
from pages.base_page import BasePage

class HeaderPage(BasePage):
    @allure.step("Нажать кнопку 'Ученику'")
    def click_ucheniku(self):
        browser.element(HeaderLocators.BUTTON_UCHENIKU).click()
        browser.should(have.url(f"{os.getenv('ROOT_URL')}ucheniku"))

    @allure.step("Нажать кнопку 'Родителю'")
    def click_roditelyu(self):
        browser.element(HeaderLocators.BUTTON_RODITELYU).click()
        browser.should(have.url(f"{os.getenv('ROOT_URL')}roditelyu"))

    @allure.step("Нажать кнопку 'Учителю'")
    def click_uchitelyu(self):
        browser.element(HeaderLocators.BUTTON_UCHITELYU).click()
        browser.should(have.url(f"{os.getenv('ROOT_URL')}uchitelyu"))

    @allure.step("Нажать кнопку 'Школе'")
    def click_shkole(self):
        browser.element(HeaderLocators.BUTTON_SHKOLE).click()
        browser.should(have.url(f"{os.getenv('ROOT_URL')}shkole"))

    @allure.step("Нажать кнопку 'Каталог'")
    def click_catalog(self):
        browser.element(HeaderLocators.BUTTON_CATALOG).click()
        browser.should(have.url(f"{os.getenv('ROOT_URL')}catalog"))
        return self

    @allure.step("Нажать кнопку 'Cart'")
    def click_cart(self):
        browser.element(HeaderLocators.BUTTON_CART).click()
        browser.should(have.url(f"{os.getenv('ROOT_URL')}cart"))
        return self