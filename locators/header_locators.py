from selenium.webdriver.common.by import By

class HeaderLocators:
    # Локаторы с использованием уникальных классов и структуры
    BUTTON_UCHENIKU = (By.CSS_SELECTOR, 'div.headerNavigationRolesItemComponent._student div.name')
    BUTTON_RODITELYU = (By.CSS_SELECTOR, 'div.headerNavigationRolesItemComponent._parent div.name')
    BUTTON_UCHITELYU = (By.CSS_SELECTOR, 'div.headerNavigationRolesItemComponent._teacher div.name')
    BUTTON_SHKOLE = (By.CSS_SELECTOR, 'div.headerNavigationRolesItemComponent._school div.name')
