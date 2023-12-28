print("Coffee, Coffee, Coffee!")

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_insufficient_resources(ingredients):
    insufficient_resources_list = []

    for k, v in ingredients.items():
        if resources[k] < v:
            insufficient_resources_list.append(k)

    return insufficient_resources_list

def make_beverage(ingredients):
    for k, v in ingredients.items():
        resources[k] -= v


while True:
    requirement = input("What would you like? 'espresso', 'latte', or 'cappuccino': ").lower()

    if requirement == "off":
        break

    if requirement == "report":
        print_report()
        continue

    if not MENU.keys().__contains__(requirement):
        print(f"unknown beverage '{requirement}', expected 'espresso', 'latte', or 'cappuccino'")
        continue

    item = MENU[requirement]

    item_ingredients= item["ingredients"]
    insufficient_resources = check_insufficient_resources(item_ingredients)

    if len(insufficient_resources) != 0:
        print(f"Sorry there is not enough {', '.join(insufficient_resources)}")
        continue

    print("Please insert coins")

    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    item_cost = item["cost"]
    if total < item_cost:
        print("Sorry that's not enough money. Money refunded.")
        continue

    if total > item_cost:
        print(f"Here is ${(total - item_cost).__round__(2)} in change.")

    money += item_cost
    make_beverage(item_ingredients)
    print(f"Here is your {requirement}. Enjoy!")

