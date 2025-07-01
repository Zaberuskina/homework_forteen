from selene import browser, have
from locators.login_page_locators import LoginPageLocators
import os
import allure


class LoginPage:
    @allure.step("Открыть страницу авторизации")
    def open(self):
        url = os.getenv('SIGNIN_URL')
        browser.open(url)

    @allure.step("Ввести логин")
    def enter_login(self, login):
        browser.element(LoginPageLocators.FIELD_LOGIN).type(login)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        browser.element(LoginPageLocators.FIELD_PASSWORD).type(password)

    @allure.step("Нажать кнопку подтверждения")
    def submit(self):
        browser.element(LoginPageLocators.BUTTON_NEXT).click()

    @allure.step("Проверить успешную авторизацию")
    def should_be_logged_in(self):
        browser.element('h1').should(have.text('Персональная информация'))
