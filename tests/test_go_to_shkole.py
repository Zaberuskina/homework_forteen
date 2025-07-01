from pages.header_page import HeaderPage


def test_go_to_shkole():
    page = HeaderPage()
    page.open()
    page.click_shkole()
