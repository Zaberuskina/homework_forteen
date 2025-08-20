from selenium.webdriver.common.by import By

class HeaderLocators:
    BUTTON_UCHENIKU = (By.CSS_SELECTOR, 'div.headerNavigationRolesItemComponent._student div.name')
    BUTTON_RODITELYU = (By.CSS_SELECTOR, 'div.headerNavigationRolesItemComponent._parent div.name')
    BUTTON_UCHITELYU = (By.CSS_SELECTOR, 'div.headerNavigationRolesItemComponent._teacher div.name')
    BUTTON_SHKOLE = (By.CSS_SELECTOR, 'div.headerNavigationRolesItemComponent._school div.name')
    BUTTON_CATALOG = (By.CSS_SELECTOR, 'a.link[href="/catalog"]')
    BUTTON_CART = (By.CSS_SELECTOR, 'a[href="/cart"]')
