import os
from pages.login_page import LoginPage


def test_login():
    login = os.getenv('LECTA_LOGIN')
    password = os.getenv('LECTA_PASSWORD')

    page = LoginPage()
    page.open()
    page.enter_login(login)
    page.enter_password(password)
    page.submit()
    page.should_be_logged_in()
