from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_handler = MoneyMachine()
coffee_menu = Menu()


drink_type = input(f"What would you like? {coffee_menu.get_items()}: ")

while drink_type != "off":

    if drink_type == "report":
        coffee_machine.report()
        money_handler.report()

    elif drink_type != "off":

        user_drink_choice = coffee_menu.find_drink(drink_type)

        #There are enough resources
        if coffee_machine.is_resource_sufficient(user_drink_choice):
            if money_handler.make_payment(user_drink_choice.cost):
                coffee_machine.make_coffee(user_drink_choice)
               
            else:
                print("Sorry, that's not enough money. Money refunded")
    
    drink_type = input(f"What would you like? {coffee_menu.get_items()}: ")

