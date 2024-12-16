import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


from main_page import MainPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.title("Проверка открытия страницы aviasales.ru и автоматическое заполнение города")
@allure.severity("medium")
def test_open_page(driver):
    current_city = "Волгоград" #Подставить город, где вы находитесь (с аэропортом)
    with allure.step("Открыть страницу"):
        main_page = MainPage(driver)
    with allure.step("Проверка автоматического заполнения города"):
        assert driver.find_element(By.ID, "avia_form_origin-input").get_attribute("value") == current_city


@allure.title("Проверка того, что открывается страница https://ostrovok.ru/ при поиске билетов")
@allure.severity("medium")
def test_hotels(driver):
    main_page = MainPage(driver)
    with allure.step("Заполнить город отправления"):
        main_page.fill_origin("Волгоград")
    with allure.step("Заполнить город назначения"):
        main_page.fill_destination("Москва")
    main_page.open_calender()
    main_page.choose_date("12.12.2024")
    main_page.click_search()
    with allure.step("Проверка того, что открывается страница https://www.aviasales.ru/ при поиске билетов"):
        assert "https://www.aviasales.ru/" in driver.current_url, "Неверный URL после поиска"


@allure.title("Проверка загаловка страницы")
@allure.severity("medium")
def test_text(driver):
    main_page = MainPage(driver)
    expected_text = "Тут покупают дешёвые авиабилеты"
    header = driver.find_element(By.CSS_SELECTOR, "h1.header__title")
    with allure.step("Проверка того, что в заголовке указан нужный текст"):
        assert header.text == expected_text


@allure.title("Негативный тест на проверку заполнения без города")
@allure.severity("critical")
def test_negative_destination(driver):
    main_page = MainPage(driver)
    main_page.click_search()
    element = driver.find_element(By.XPATH, '//div[text()="Укажите город прибытия"]')
    with allure.step("Проверка того, что незаполненное поле Куда подcвечивается"):
        assert element.is_displayed()


@allure.title("Негативный тест на проверку заполнения без даты")
@allure.severity("critical")
def test_negative_date(driver):
    main_page = MainPage(driver)
    main_page.click_search()
    element = driver.find_element(By.XPATH, '//div[text()="Укажите дату"]')
    with allure.step("Проверка того, что незаполненное поле Дата подcвечивается"):
        assert element.is_displayed()
