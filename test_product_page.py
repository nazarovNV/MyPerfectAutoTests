import time

import pytest

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    # Перед тестом срабатывает фикстура browser в которой в browser присваивается ссылка на драйвер.
    # Инициализируем адрес страницы.
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    # Создаем экземпляр класса ProductPage, который наследуется от базового класса BasePage.
    # В BasePage находится конструктор в котором инициализируются переменные browser и link.
    page = ProductPage(browser, link)
    # Открываем страницу.
    page.open()
    # Добавляем товар в корзину.
    page.add_to_card()
    # Решаем уравнение и закрываем окно алерта.
    page.solve_quiz_and_get_code()
    # Проверяем что товар находится в корзине.
    page.is_good_in_basket(page.get_good_name())
    # Проверяем что цена товара в корзине соответствует цене товара из витрины магазина.
    page.is_good_price_equal_basket_price(page.get_good_price())
    # После теста срабатывает код из фикстуры browser,
    # который находится после yield в результате чего окно браузера закрывается.


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_user_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    # Перед тестом срабатывает фикстура browser в которой в browser присваивается ссылка на драйвер.
    # Инициализируем адрес страницы.
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # Создаем экземпляр класса ProductPage, который наследуется от базового класса BasePage.
    # В BasePage находится конструктор в котором инициализируются переменные browser и link.
    page = ProductPage(browser, link)
    # Открываем страницу.
    page.open()
    # Проверяем что есть ссылка на страницу для входа в профиль
    page.should_be_login_link()
    # После теста срабатывает код из фикстуры browser,
    # который находится после yield в результате чего окно браузера закрывается.


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # Перед тестом срабатывает фикстура browser в которой в browser присваивается ссылка на драйвер.
    # Инициализируем адрес страницы.
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # Создаем экземпляр класса ProductPage, который наследуется от базового класса BasePage.
    # В BasePage находится конструктор в котором инициализируются переменные browser и link.
    page = ProductPage(browser, link)
    # Открываем страницу.
    page.open()
    # Проверяем что есть ссылка на страницу для входа в профиль.
    page.should_be_login_link()
    # Переходим на страницу входа и регистрации.
    page.go_to_login_page()
    # Инициализируем новую страницу.
    login_page = LoginPage(browser, browser.current_url)
    # Проверяем что мы находимся на странице входа и регистрации.
    login_page.should_be_login_page()
    # После теста срабатывает код из фикстуры browser,
    # который находится после yield в результате чего окно браузера закрывается.


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Перед тестом срабатывает фикстура browser в которой в browser присваивается ссылка на драйвер.
    # Инициализируем адрес страницы.
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # Создаем экземпляр класса ProductPage, который наследуется от базового класса BasePage.
    # В BasePage находится конструктор в котором инициализируются переменные browser и link.
    page = ProductPage(browser, link)
    # Открываем страницу.
    page.open()
    # Переходим на страницу корзины.
    page.go_to_basket()
    # Инициализируем новую страницу.
    basket_page = BasketPage(browser, browser.current_url)
    # Проверяем что корзина пуста.
    basket_page.should_not_be_goods_in_basket()
    # Проверяем, что есть тест о том, что корзина пуста.
    basket_page.should_be_text_empty()
    # После теста срабатывает код из фикстуры browser,
    # который находится после yield в результате чего окно браузера закрывается.


# Класс который нужен для объединения тестов для авторизованного пользователя
class TestUserAddToBasketFromProductPage:
    # Фикстура которая срабатывает каждый раз когда вызываются методы класса.
    # С помощью этой фикстуры перед тестами проиходит регистрация пользователя и потом авторизация
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Инициализируем пароль.
        password = "R%2375491"
        # Инициализируем рандомный эмейл.
        email = str(time.time()) + "@fakemail.org"
        # Инициализируем адрес страницы.
        link = "http://selenium1py.pythonanywhere.com/"
        # Создаем экземпляр класса ProductPage, который наследуется от базового класса BasePage.
        # В BasePage находится конструктор в котором инициализируются переменные browser и link.
        page = MainPage(browser, link)
        # Открываем страницу.
        page.open()
        # Переходим на страницу входа и регистрации.
        page.go_to_login_page()
        # Инициализируем новую страницу.
        login_page = LoginPage(browser, browser.current_url)
        # Регистрируем нового пользователя.
        login_page.register_new_user(email, password)
        # Инициализируем новую страницу.
        main_page = MainPage(browser, browser.current_url)
        # Проверяем что пользователь авторизовался.
        main_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # Перед тестом срабатывает фикстура browser в которой в browser присваивается ссылка на драйвер.
        # Также перед тестом срабатывает фикстура setup с помощью которой
        # регистрируется и авторизуется пользователь.
        # Инициализируем адрес страницы.
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        # Создаем экземпляр класса ProductPage, который наследуется от базового класса BasePage.
        # В BasePage находится конструктор в котором инициализируются переменные browser и link.
        page = ProductPage(browser, link)
        # Открываем страницу.
        page.open()
        # Добавляем товар в корзину.
        page.add_to_card()
        # Решаем уравнение и закрываем окно алерта.
        page.solve_quiz_and_get_code()
        # Проверяем что товар находится в корзине.
        page.is_good_in_basket(page.get_good_name())
        # Проверяем что цена товара в корзине соответствует цене товара из витрины магазина.
        page.is_good_price_equal_basket_price(page.get_good_price())
        # После теста срабатывает код из фикстуры browser,
        # который находится после yield в результате чего окно браузера закрывается.
