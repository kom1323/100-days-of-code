


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

machine_profit = 0



def PrintReport() -> None:
    print(  f"Water: {resources['water']}ml\n" + 
            f"Milk: {resources['milk']}ml\n" +
            f"Coffee: {resources['coffee']}g\n" + 
            f"Money: ${machine_profit}"

    )


def CheckResources(drink) -> bool:

    if drink == "espresso":
        water = 50
        coffee = 18
        milk = 0
    elif drink == "latte":
        water = 200
        coffee = 24
        milk = 150
    else:
        #drink is cappuccino
        water = 250
        coffee = 24
        milk = 100
    
    if resources["water"] - water < 0: 
        print("Sorry there is not enough water.")
        return False
    if resources["coffee"] - coffee < 0:
        print("Sorry there is not enough coffee.")
        return False
    if resources["milk"] - milk < 0:
        print("Sorry there is not enough milk")
        return False
    return True


def GetDrinkPrice(drink_type) -> float:
    
    if drink_type == "espresso":
        return 1.5
    elif drink_type == "latte":
        return 2.5
    else:
        #drink is cappuccino
        return 3


def ProcessCoins(drink_type) -> float:

    """recives user money and returns the remainder of the money"""

    drink_cost = GetDrinkPrice(drink_type)

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    quarters = 0.25 * quarters
    dimes = 0.1 * dimes
    nickles = 0.05 * nickles
    pennies = 0.01 * pennies

    sum = quarters + dimes + nickles + pennies

    return sum - drink_cost

def MakeCoffee(drink_type):
    if drink_type == "espresso":
        water = 50
        coffee = 18
        milk = 0
    elif drink_type == "latte":
        water = 200
        coffee = 24
        milk = 150
    else:
        #drink is cappuccino
        water = 250
        coffee = 24
        milk = 100

    resources["water"] -= water
    resources["coffee"] -= coffee 
    resources["milk"] -= milk 

    


#add loop to service
drink_type = input("What would you like? (espresso/latte/cappuccino): ")

while drink_type != "off":

    if drink_type == "report":
        PrintReport()

    elif drink_type != "off":

        #There are enough resources
        if CheckResources(drink_type):
            change = ProcessCoins(drink_type)
            if change >= 0:
                MakeCoffee(drink_type)
                drink_cost = GetDrinkPrice(drink_type)
                machine_profit += drink_cost

                if change > 0:
                    print(f"Here is ${'{:.2f}'.format(change)} in change.")
                else:
                    print("No change.")
                print(f"Here is your {drink_type} ☕. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded")
    
    drink_type = input("What would you like? (espresso/latte/cappuccino): ")


