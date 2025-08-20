# Автоматизированные UI-тесты для домашего задания  QA quru

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.25.0-green.svg)
![Allure](https://img.shields.io/badge/allure-2.13.5-orange.svg)

## 📌 О проекте

Автоматизированные тесты для веб-интерфейса образовательной платформы, покрывающие:
- Авторизацию пользователей
- Навигацию между ролями (Ученик, Учитель, Родитель, Школа)
- Проверку переходов между страницами

## 🛠 Технологический стек

- **Python 3.9+** - язык программирования
- **Selenium WebDriver** - автоматизация браузера
- **Selene** - удобная обертка над Selenium
- **Pytest** - фреймворк для тестирования
- **Allure** - генератор отчетов
- **Jenkins** - система непрерывной интеграции
- **Selenoid** - контейнеризованный запуск браузеров

## 📂 Структура проекта
project/
├── .env # Файл с переменными окружения  
├── pytest.ini # Конфигурация Pytest  
├── requirements.txt # Зависимости Python  
├── Jenkinsfile # Конфигурация Jenkins  
├── pages/ # Page Object модели  
│ ├── base_page.py # Базовые методы   
│ ├── header_page.py # Шапка сайта  
│ └── login_page.py # Страница авторизации  
├── locators/ # Локаторы элементов  
│ ├── header_locators.py # Локаторы шапки  
│ └── login_page_locators.py # Локаторы логина  
├── tests/ # Тесты  
│ ├── test_go_to_ucheniku.py # Тесты раздела "Ученику"  
│ ├── test_go_to_roditelyu.py # Тесты раздела "Родителю"  
│ ├── test_go_to_uchitelyu.py # Тесты раздела "Учителю"  
│ ├── test_go_to_shkole.py # Тесты раздела "Школе"
│ └── test_login.py # Тесты авторизации  
   ├── test_go_to_catalog.py # Тесты раздела "Каталог"
   ├── test_go_to_cart.py # Тесты раздела "Корзина"
└── utils/ # Вспомогательные утилиты  
└── attach.py # Генерация аттачментов для Allure  
## 🌐 CI/CD и Мониторинг

### <img src="https://jenkins.io/images/logos/jenkins/jenkins.svg" width="20"> **Jenkins Pipeline**

**Ссылка на сборку**:  
[https://jenkins.autotests.cloud/job/homework_forteen_ANikashova/](https://jenkins.autotests.cloud/job/homework_forteen_ANikashova/)

**Особенности пайплайна**:
- Автоматический запуск тестов в Selenoid
- Генерация Allure-отчёта
- Отправка уведомлений в Telegram

### <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="20"> Allure Report
**Пример отчёта**:  
[https://jenkins.autotests.cloud/job/homework_forteen_ANikashova/4/allure/](https://jenkins.autotests.cloud/job/homework_forteen_ANikashova/4/allure/)

![img_2.png](img_2.png)

### <img src="https://telegram.org/img/t_logo.png" width="20"> Telegram Bot
**Бот для уведомлений**:  
[@homework_13_Nikashova_bot](https://t.me/homework_13_Nikashova_bot)
![img_1.png](img_1.png)
