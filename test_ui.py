import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

from main_page import MainPage

@allure.title("Проверка открытия страницы aviasales.ru и автоматическое заполнение города")
@allure.severity("medium")
def test_open_page():
    current_city = "Саратов" #Подставить город, где вы находитесь (с аэропортом)
    with allure.step("Открыть страницу"):
        main_page = MainPage(driver)
    with allure.step("Проверка автоматического заполнения города"):
        assert driver.find_element(By.ID, "avia_form_origin-input").get_attribute("value") == current_city
    driver.quit()

@allure.title("Проверка того, что открывается страница https://ostrovok.ru/ при поиске билетов")
@allure.severity("medium")
def test_hotels():
    main_page = MainPage(driver)
    with allure.step("Заполнить город отправления"):
        main_page.fill_origin("Саратов")
    with allure.step("Заполнить город назначения"):
        main_page.fill_destination("Новокузнецк")
    main_page.open_calender()
    main_page.choose_date("12.12.2024")
    main_page.click_search()
    with allure.step("Проверка того, что открывается страница https://www.aviasales.ru/ при поиске билетов"):
        assert "https://www.aviasales.ru/" in driver.current_url
    driver.quit()

@allure.title("Проверка загаловка страницы")
@allure.severity("medium")
def test_text():
    main_page = MainPage(driver)
    expected_text = "Тут покупают дешёвые авиабилеты"
    header = driver.find_element(By.CSS_SELECTOR, "h1.header__title")
    with allure.step("Проверка того, что в заголовке указан нужный текст"):
        assert header.text == expected_text
    driver.quit()

@allure.title("Негативный тест на проверку заполнения без города")
@allure.severity("critical")
def test_negative_destination():
    main_page = MainPage(driver)
    main_page.click_search()
    element = driver.find_element(By.XPATH, '//div[text()="Укажите город прибытия"]')
    with allure.step("Проверка того, что незаполненное поле Куда подcвечивается"):
        assert element.is_displayed()
    driver.quit()

@allure.title("Негативный тест на проверку заполнения без даты")
@allure.severity("critical")
def test_negative_date():
    main_page = MainPage(driver)
    main_page.click_search()
    element = driver.find_element(By.XPATH, '//div[text()="Укажите дату"]')
    with allure.step("Проверка того, что незаполненное поле Дата подcвечивается"):
        assert element.is_displayed()
    driver.quit()