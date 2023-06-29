#Importing the classes that are defined in other files.
from menu import Menu
from resources import Resources
from cashregister import CashRegister

#Setting each class equal to a variable.
cash_register = CashRegister()
resources = Resources()
menu = Menu()

#Setting is_on equal to True.
is_on = True

#While loop that runs whilst is_on is set to True and sets options equal to get_items() instance method from the imported
#Menu class. Choice is set equal to an input variable that presents the user with options of strong/medium/weak and then sets
#choice equal to their answer. If choice == "off" then is on = False so the while loop ends. if choice == report then the
#then the report instance method from the imported Resources class is called and the report instance method from the imported
#Cash_Register class is called. If the else statement is true then drink is set equal to the find_drink instance method of the imported
#Menu class with the order_name being set to the users choice of drink. However the drink will only be made if there are
#sufficient resources and the user has enough money.
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        resources.report()
        cash_register.report()
    else:
        drink = menu.find_drink(choice)

        if resources.is_resource_sufficient(drink) and cash_register.make_payment(drink.cost):
            resources.make_drink(drink)