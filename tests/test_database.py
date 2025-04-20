from data import TestDataBase
from conftest import db
import pytest
import allure


class TestDB:
    @allure.title('Проверка работы метода available_buns, который показывает доступные булочки из базы данных')
    @allure.description('Выполняем три теста - проверяем имя и стоимость каждой булки')
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestDataBase.test_data_base_buns)
    def test_available_buns_db_success(self, db, index_bun, bun_name, bun_price):
        data_buns = db.available_buns()
        assert data_buns[index_bun].get_name() == bun_name and data_buns[index_bun].get_price() == bun_price

    @allure.title('Проверка работы метода available_ingredients, который показывает доступные ингредиенты из базы данных')
    @allure.description('Выполняем шесть тестов - проверяем имя, тип и стоимость каждого ингредиента')
    @pytest.mark.parametrize('index_ingredient, type_ingredient, name_ingredient, price_ingredient', TestDataBase.test_data_base_ingredients)
    def test_available_ingredients_db_success(self, db, index_ingredient, type_ingredient, name_ingredient, price_ingredient):
        data_ingredients = db.available_ingredients()
        assert (data_ingredients[index_ingredient].get_name() == name_ingredient and
                data_ingredients[index_ingredient].get_type() == type_ingredient and
                data_ingredients[index_ingredient].get_price() == price_ingredient)
