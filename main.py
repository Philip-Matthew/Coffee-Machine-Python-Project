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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(drink):
    for item in resources:
        if MENU[drink]['ingredients'][item] < resources[item]:
            return True
    else:
        return False


def process_coins():
    global total
    print("Insert Coins...")
    total = int(input("How many quaters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def make_coffee():
    global profit
    profit += MENU[drink]["cost"]
    for item in resources:
        resources[item] -= MENU[drink]['ingredients'][item]
    print(f"Here's your {drink}. Ready!")


def is_transaction_successful():
    if total == MENU[drink]["cost"]:
        make_coffee()
    elif total < MENU[drink]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        change = total - MENU[drink]["cost"]
        print(f"Here's your change ${change}")
    return True


is_on = True

while is_on:
    user_prompt = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_prompt == "off":
        is_on = False
        break
    elif user_prompt == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
    else:
        drink = user_prompt
        if is_resources_sufficient(drink):
            payment = process_coins()
            if is_transaction_successful():
                make_coffee()
