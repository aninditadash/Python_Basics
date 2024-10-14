from contents import pantry, recipes

def add_shopping_item(data: dict, item_to_buy: str, item_quantity: int) -> None:
    """
    Add a tuple containing item and quantity in the shopping_list
    :param data: dictionary containing the shopping list items
    :param item_to_buy: item
    :param item_quantity: quantity
    """
    # setdefault() returns the value from the dictionary if key exists, if key doesn't exist, creates a new
    # entry for the key and assigns the default value to it and returns the default value
    data[item_to_buy] = data.setdefault(item_to_buy, 0) + item_quantity


display_dict_loop = {}
for index, meal in enumerate(recipes):
    display_dict_loop[str(index + 1)] = meal

display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

print(f"display_dict_loop - {display_dict_loop}")
print(f"display_dict - {display_dict}")

# Create empty dictionary for the items to buy
shopping_list = {}

while True:
    # Display the recipes
    print("Please choose the recipies: ")
    for key, value in display_dict.items():
        print(f"{key}: {value}")
    print("0: To quit")

    choice = input("> ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        ingredients = recipes[selected_item]
        print(f"checking ingredients...{ingredients}")
        for food_item, required_qty in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_qty <= quantity_in_pantry:
                print(f"{food_item} found with quantity needed - {required_qty}")
            else:
                quantity_to_buy = required_qty - quantity_in_pantry
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

print("Need to buy following items...")
for item, quantity in shopping_list.items():
    print(f"{item} - {quantity}")

