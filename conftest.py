import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# обработчик опции в функции
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, en, ...etc")

# фикстура которая будет выполняться для метода теста до и после
@pytest.fixture(scope="function")
def browser(request):
    # запрос значения параметра language
    language_name = request.config.getoption("language")
    # создаем экземпляр класса Options
    options = Options()
    # передаем браузеру значение языка страницы
    options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    # инициализируем драйвер
    browser = webdriver.Chrome(options=options)
    # код после yield будет выполняться после прохождения теста
    yield browser
    # закрываем браузер
    browser.quit()