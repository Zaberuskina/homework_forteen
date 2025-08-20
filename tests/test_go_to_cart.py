from pages.header_page import HeaderPage

def test_go_to_cart():
    page = HeaderPage()
    page.open()
    page.click_cart()