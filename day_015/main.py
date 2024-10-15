from data import menu, resources

profit = 0


def is_resource_sufficient(order_ingredients):
    """
    Check if there are enough resources to make the drink.

    :param order_ingredients: A dictionary containing the ingredients required for the order.
    :return: True if there are enough resources, False otherwise.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Prompt the user to insert coins and calculate the total amount of money received.

    :return: The total amount of money received from the inserted coins.
    """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Determine if the transaction is successful based on the money received and the drink cost.

    :param money_received: The amount of money received from the customer.
    :param drink_cost: The cost of the drink.
    :return: True if the transaction is successful (i.e., money received is sufficient), False otherwise.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Deduct the required ingredients from the resources to make the drink and print a message.

    :param drink_name: The name of the drink to be made.
    :param order_ingredients: A dictionary containing the ingredients required for the order.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def main():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = menu[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])


main()
