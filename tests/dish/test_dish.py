from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501
from tests.ingredients import INGREDIENTS
import pytest


# Req 2
def test_dish():
    ingredients_list = list(INGREDIENTS)
    dish_1 = Dish("lasanha berinjela", 27.00)
    dish_1_1 = Dish("lasanha berinjela", 27.00)
    dish_2 = Dish("lasanha presunto", 25.90)
    tomato = Ingredient("tomate")

    assert dish_1.name == "lasanha berinjela"
    assert dish_1.__hash__() == dish_1_1.__hash__()
    assert dish_1.__hash__() != dish_2.__hash__()
    assert dish_1 == dish_1_1
    assert dish_1 != dish_2
    assert dish_1.__repr__() == "Dish('lasanha berinjela', R$27.00)"
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("lasanha berinjela", "27.00")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("lasanha berinjela", -27.00)
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("lasanha berinjela", 0)

    for index, ingredient in enumerate(ingredients_list):
        dish_1.add_ingredient_dependency(ingredient, index + 1)
    assert dish_1.recipe.get(tomato) == 2

    assert dish_1.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert dish_1.get_ingredients() == set(ingredients_list)
