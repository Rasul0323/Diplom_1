from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class BunData1:
    bun_name = 'Флюоресцентная булка R2-D3'
    bun_price = 988
    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус традиционный галактический'
    sauce_price = 15

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Говяжий метеорит (отбивная)'
    filling_price = 3000

    burger_final_cost = bun_price * 2 + sauce_price + filling_price

class BunData2:
    bun_name = 'Краторная булка N-200i'
    bun_price = 1255

    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус фирменный Space Sauce'
    sauce_price = 80

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Филе Люминисцентного тетраодонтимформа'
    filling_price = 988

    burger_final_cost = bun_price * 2 + sauce_price + filling_price

