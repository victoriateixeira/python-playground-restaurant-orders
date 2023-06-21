import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = set()
        self.create_menu_item()

    def create_menu_item(self):
        with open(self.path, encoding="utf-8") as file:
            menu_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            group_by_dish = {}
            for row in menu_reader:
                dish = row["dish"]
                price = float(row["price"])
                ingredient = row["ingredient"]
                amount = int(row["recipe_amount"])
                if dish not in group_by_dish:
                    group_by_dish[dish] = {
                        "price": price,
                        "ingredients": [(ingredient, amount)],
                    }
                group_by_dish[dish]["ingredients"].append((ingredient, amount))

        for key in group_by_dish:
            new_dish = Dish(key, group_by_dish[key]["price"])
            for ingredient, amount in group_by_dish[key]["ingredients"]:
                ingredient_class = Ingredient(ingredient)
                new_dish.add_ingredient_dependency(ingredient_class, amount)
            self.dishes.add(new_dish)
