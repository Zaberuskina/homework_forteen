from pages.header_page import HeaderPage
from selene import browser

def test_go_to_uchitelyu():
    page = HeaderPage()
    page.open()
    page.click_uchitelyu()
