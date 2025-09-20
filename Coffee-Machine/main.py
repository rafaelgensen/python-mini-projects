from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

while True:
    order = input("What would you like? (espresso/latte/cappuccino):")
    drink = menu.find_drink(order)
    if order == "report":
        coffee.report()
        money.report()
        continue
    if order == "off":
        break
    if drink is not None:
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
