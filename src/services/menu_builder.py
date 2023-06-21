from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)
        print(self.menu_data.dishes)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        dishes_list = self.menu_data.dishes
        # complete_menu = []
        filtered_menu = []
        for dish in dishes_list:
            ingredients = dish.get_ingredients()
            restrictions = dish.get_restrictions()
            menu_item = {
                "dish_name": dish.name,
                "ingredients": ingredients,
                "price": dish.price,
                "restrictions": restrictions,
            }
            if restriction:
                if restriction not in restrictions:
                    filtered_menu.append(menu_item)

            else:
                filtered_menu.append(menu_item)
        return filtered_menu


menu = MenuBuilder()
print(menu)
