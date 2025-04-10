import allure
from conftest import *

class TestBun:

    @allure.title('Проверка метода get_name, который используется для получения названия булки')
    def test_get_name_check_the_name_success(self, mock_bun):
        assert mock_bun.get_name() == BunData1.bun_name

    @allure.title('Проверка работы метода get_price, который используется для получения цены булки')
    def test_get_price_check_the_price_success(self, mock_bun_2):
        assert mock_bun_2.get_price() == BunData2.bun_price
