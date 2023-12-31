from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Coffee, Coffee, Coffee!")

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    requirement = input(f"What would you like? {menu.get_items()}: ").lower()

    if requirement == "off":
        break

    if requirement == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    item = menu.find_drink(requirement)

    if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
        coffee_maker.make_coffee(item)
