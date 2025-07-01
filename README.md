# Проект автоматизации тестирования покупки товаров на Lecta


Этот проект предназначен для автоматизации тестирования покупки товаров на [Lecta](https://stage.lecta.ru/) с использованием Selenium, Pytest и Allure.
В  [данной задаче](https://jira.prosv.ru/browse/LECTA-265) приложен цикл ручных тест-кейсов, которые в дальнейшнем легли в основу данных автотестов
## Содержание

- [Установка](#установка)
- [Структура проекта](#структура-проекта)
- [Запуск автотестов и генерация отчетов Allure](#запуск-тестов и генерация-отчетов-allure)

## Установка

1. **Клонируйте репозиторий:**
   ```sh
   git clone https://git.prosv.ru/qa/lectaui/lectacart.git
   cd lectacart
2. **Создайте виртуальное окружение и активируйте его:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # для Unix/MacOS
   .\venv\Scripts\activate  # для Windows
3. **Установите зависимости:**
   ```sh
   pip install -r requirements.txt
4. **Установите Allure Commandline:**
    ```sh
   Скачайте и установите Allure Commandline с официального сайта: Allure Commandline.
    Добавьте путь к Allure Commandline в переменную окружения PATH.

## Структура проекта
project/
│
├── locators/
│   ├── cart_locators.py
│   ├── catalog_locators.py
│   ├── login_page_locators.py
│   ├── yookassa_locators.py
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── cart_page.py
│   ├── catalog_page.py
│   ├── login_page.py
│   ├── yookassa_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_add_to_cart.py
│   ├── test_purchase_from_cart.py
│   ├── test_purchase_gift.py
│   ├── test_purchase_promocode.py
│
├── data.py
├── conftest.py
├── .gitignore
├── README.md
├── requirements.txt

## Запуск автотестов и генерация отчетов Allure
1. **Убедитесь, что находитесь в нужной директории:**
    ```sh
   cd..#выход из директории
   cd *название директории*#вход в директорию
2. **Запустите тесты с Pytest и сохраните результаты в директорию allure-results::**
    ```sh
   pytest --alluredir=allure-results
3. **Сгенерируйте и откройте отчет Allure:**
    ```sh
   allure serve allure-results

