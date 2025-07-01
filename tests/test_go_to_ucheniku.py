from pages.header_page import HeaderPage


def test_go_to_ucheniku():
    page = HeaderPage()
    page.open()
    page.click_roditelyu()
    page.click_ucheniku()
