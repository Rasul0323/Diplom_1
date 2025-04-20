from conftest import *
import allure


class TestIngredient:
    @allure.title('Проверка работы метода get_name, который получает название соуса')
    def test_get_name_sauce_success(self, mock_sauce):
        assert mock_sauce.get_name() == BunData1.sauce_name

    @allure.title('Проверка работы метода get_name, который получает название начинки')
    def test_get_name_filling_success(self, mock_filling):
        assert mock_filling.get_name() == BunData1.filling_name

    @allure.title('Проверка работы метода get_price, который получает цену соуса')
    def test_get_price_sauce_success(self, mock_sauce_2):
        assert mock_sauce_2.get_price() == BunData2.sauce_price

    @allure.title('Проверка работы метода get_price, который получает цену начинки')
    def test_get_price_filling_success(self, mock_filling_2):
        assert mock_filling_2.get_price() == BunData2.filling_price

    @allure.title('Проверка работы метода get_type, который получает тип ингредиента для соуса')
    def test_get_type_sauce_success(self, mock_sauce):
        assert mock_sauce.get_type() == BunData1.sauce_type

    @allure.title('Проверка работы метода get_type, который получает тип ингредиента для начинки')
    def test_get_type_filling_success(self, mock_filling):
        assert mock_filling.get_type() == BunData1.filling_type
