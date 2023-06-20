from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient1_1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("tomate")
    assert ingredient1.name == "queijo mussarela"
    assert ingredient1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert ingredient1.__hash__() == ingredient1_1.__hash__()
    assert ingredient1.__hash__() != ingredient2.__hash__()
    assert ingredient1 == ingredient1_1
    assert ingredient1 != ingredient2
    assert ingredient1.__repr__() == "Ingredient('queijo mussarela')"
