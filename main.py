# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# def is_resource_sufficient(order_ingredients):
#     """Returns true when order can be made and false if ingredients are not sufficient"""
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry, there is not enough {item}.")
#             return False
#     return True
#
# def process_coins():
#     """Returns the total calculated from coins inserted"""
#     print("Please insert coins:")
#     total = int(input("How many quarters?:")) * 0.25
#     total += int(input("How many dines?:")) * 0.1
#     total += int(input("How many nickels?:")) * 0.05
#     total += int(input("How many pennies?:")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received,drink_cost):
#     """Returns true when payment is accepted and false if money is insufficient"""
#     if money_received>=drink_cost:
#         change=round(money_received - drink_cost,2)
#         print(f"Here is ${change}")
#         global profit
#         profit+= drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money.Money refunded")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources"""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name}")
#
# is_on = True
# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino):")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink['ingredients']):
#             payment = process_coins()
#         if is_transaction_successful(payment,drink['cost']):
#             make_coffee(choice, drink["ingredients"])
#
#
#
#
#
#

import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





