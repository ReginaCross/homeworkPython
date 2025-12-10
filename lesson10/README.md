Автоматизация тестирования с Page Object Pattern и Allure
Описание проекта
Проект содержит автоматизированные тесты для двух веб-приложений:
1.	Калькулятор с задержкой
2.	Интернет-магазин SauceDemo
Тесты написаны с использованием:
•	Python 3.8+
•	Selenium WebDriver
•	Page Object Pattern
•	Allure для отчетов
•	Pytest как тестовый фреймворк


Структура проекта
├── pages/                    # Классы Page Object
│   ├── calculator_page.py    # Страница калькулятора
│   └── saucedemo/           # Страницы SauceDemo
├── tests/                    # Тесты
│   ├── test_calculator.py   # Тесты калькулятора
│   └── test_saucedemo.py    # Тесты магазина
├── conftest.py              # Pytest конфигурация
├── requirements.txt         # Зависимости
└── README.md               # Документация

Требования
•	Python 3.8+
•	Google Chrome
•	Установленные зависимости из requirements.txt
Установка
1.	Клонируйте репозиторий:
git clone <repository-url>
cd project
2.	Установите зависимости:
pip install -r requirements.txt
3.	Установите Allure командной строки.
Запуск тестов
Все тесты
pytest tests/ --alluredir=allure-results
Конкретные тесты
# Тесты калькулятора
pytest tests/test_calculator.py -v --alluredir=allure-results

# Тесты магазина
pytest tests/test_saucedemo.py -v --alluredir=allure-results
С параллельным запуском
pytest tests/ -n 2 --alluredir=allure-results
Генерация отчета Allure
1.	Сгенерируйте отчет:
allure generate allure-results -o allure-report --clean
2.	Откройте отчет:
allure open allure-report
3.	Или запустите веб-сервер:
allure serve allure-results

