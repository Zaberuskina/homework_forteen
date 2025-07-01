from selenium.webdriver.common.by import By

class LoginPageLocators:
    BUTTON_LOGIN_HEADER = (By.XPATH, '//button[@class="buttonComponent" and .//div[@class="text" and text()="Войти"]]')
    FIELD_LOGIN = (By.NAME, "identifier")
    FIELD_PASSWORD = (By.NAME, "password")
    BUTTON_NEXT = (By.XPATH, '//button[@type="submit" and @class="btn" and text()="Войти или зарегистрироваться"]')
