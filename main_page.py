from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.aviasales.ru/")
        self.driver.maximize_window()

    def fill_origin(self, origin: str) -> None:
        """Заполнение поля Откуда"""
        self.element_origin = self.driver.find_element(By.ID, "avia_form_origin-input")
        self.element_origin.clear()
        self.element_origin.send_keys(origin)

    def fill_destination(self, destination: str) -> None:
        """Заполнение поля Куда"""
        self.driver.find_element(By.ID, "avia_form_destination-input").send_keys(destination)

    def open_calender(self) -> None:
        """Открытие календаря"""
        self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="departure-calendar-icon"]').click()

    def choose_date(self, date: str) -> None:
        """Выбор даты"""
        self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="date-{date}"]').click()

    def choose_passangers_quantity(self) -> None:
        """Выбор количества пассажиров"""
        self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="passengers-field"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="increase-button"]').click()

    def choose_first_class(self) -> None:
        """Выбор первого класса"""
        self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="passengers-field"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="trip-class-F"]').click()

    def choose_comfort_class(self) -> None:
        """Выбор класса комфорт"""
        self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="passengers-field"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="trip-class-W"]').click()

    def click_search(self) -> None:
        """Нажать кнопку Найти"""
        self.driver.find_element(By.CSS_SELECTOR, '[data-test-id="form-submit"]').click()

    def waiter(self) -> None:
        """Ожидание окрашивания полей"""
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'[value={self.element_origin}]'))
        )

    def get_origin_value(self) -> str:
        """Получение значения поля Откуда"""
        return self.driver.find_element(By.ID, "avia_form_destination-input").get_attribute("value")

    def get_destination_value(self) -> str:
        """Получение значения поля Откуда"""
        return self.driver.find_element(By.ID, "avia_form_origin-input").get_attribute("value")

    def get_passengers_quantity(self) -> str:
        """Получение количества пассажиров"""
        return self.driver.find_element(By.XPATH, "(//div[@aria-label='passengers'])[1]")

    def get_class(self) -> str:
        """Получение класса"""
        return self.driver.find_element(By.XPATH, "(//div[@data-test-id='trip-class'])[1]")