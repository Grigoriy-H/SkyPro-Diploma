import allure
import requests


baseURL = "https://www.aviasales.ru/"
baseURL_api = "https://min-prices.aviasales.ru/price_matrix?"
my_headers = {
    "Content-Type": "application/json"
}

@allure.title("Поиск билета в одну сторону - позитивная проверка")
@allure.feature("GET")
@allure.severity("blocker")
def test_get_oneway_positive() -> str:
    city1 = "MOW"
    city2 = "STW"
    date = "2024-12-15"
    with allure.step("Получение списка билетов в одну сторону"):
        tickets_list = requests.get(baseURL_api + f'origin_iata={city1}&destination_iata={city2}&depart_start={date}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers)
    lst = tickets_list.json()
    with allure.step("Проверка"):
        assert len(lst) > 0
        assert tickets_list.status_code == 200, "Некорректный статус-код"

@allure.title("Поиск билета в обе стороны - позитивная проверка")
@allure.feature("GET")
@allure.severity("blocker")
def test_get_twoways_positive() -> str:
    city1 = "MOW"
    city2 = "STW"
    date1 = "2024-12-15"
    date2 = "2024-12-25"
    with allure.step("Получение списка билетов в обе стороны"):
        tickets_list = requests.get(baseURL_api + f'origin_iata={city1}&destination_iata={city2}&depart_start={date1}&return_start={date2}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers)
    lst = tickets_list.json()
    with allure.step("Проверка"):
        assert len(lst) > 0
        assert tickets_list.status_code == 200, "Некорректный статус-код"

@allure.title("Поиск билета с числом 31 месяца с 31 днями - позитивная проверка")
@allure.feature("GET")
@allure.severity("blocker")
def test_get_date_31_positive() -> str:
    city1 = "MOW"
    city2 = "STW"
    date1 = "2024-12-15"
    date2 = "2024-12-31"
    with allure.step("Получение списка билетов на дату 31 месяца с 31 днями"):
        tickets_list = requests.get(baseURL_api + f'origin_iata={city1}&destination_iata={city2}&depart_start={date1}&return_start={date2}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers)
    lst = tickets_list.json()
    with allure.step("Проверка"):
        assert len(lst) > 0
        assert tickets_list.status_code == 200, "Некорректный статус-код"

@allure.title("Поиск билета с числом 31 месяца с 30 днями - негативная проверка")
@allure.feature("GET")
@allure.severity("blocker")
def test_get_date_31_negative() -> str:
    city1 = "MOW"
    city2 = "NOZ"
    date = "2024-11-31"
    with allure.step("Проверка даты 31 для месяца с 30 днями"):
        resp = requests.get(baseURL_api + f'origin_iata={city1}&destination_iata={city2}&depart_start={date}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers)
    with allure.step("Проверка"):
        assert resp.status_code == 400

@allure.title("Поиск билета в город с невалидным кодом - негативная проверка")
@allure.feature("GET")
@allure.severity("blocker")
def test_get_invalid_city_code() -> str:
    city1 = "MOW"
    city2 = "QWE"
    date = "2024-11-30"
    with allure.step("Проверка невалидного кода города"):
        resp = requests.get(baseURL_api + f'origin_iata={city1}&destination_iata={city2}&depart_start={date}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers)
    with allure.step("Проверка"):
        assert resp.status_code == 400