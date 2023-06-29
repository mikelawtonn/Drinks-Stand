#This class models the resources needed to make the drinks. The init method consists of an instance variable called resources which
#is defined as a set of three values - ice, water and orange.
class Resources:
    def __init__(self):
        self.resources = {
            "ice": 200,
            "water": 150,
            "orange": 100,
        }
    #This method prints a report of all resources. It takes the value of each individual ingredient from the resources instance
    #variable within the Resources class and prints it to screen using string formatting to insert the value of the resource
    #into the string.
    def report(self):
        print(f"Ice: {self.resources['ice']}g")
        print(f"Water: {self.resources['water']}ml")
        print(f"Orange: {self.resources['orange']}ml")

    #The instance method is_resource_sufficient has one attribute other than self and this is drink.
    #This method returns True when order can be made but False if ingredients are insufficient.
    #Initially, the can_make variable is set to true. The for loop uses drink.ingredients
    #which essentially uses the drink instance attribute combined with the list of ingredients form the MenuItem class
    #to tell the for loop how many times to run in this case it will be three as there are three ingredients
    #(water, ice and orange). if drink.ingredients[item] > self.resources[item] compares the current amount of resources
    #with the amount of resources needed to make the drink. If resources are insuffcient then a formatted string is printed
    #informing the user there is not enough of a particular item and can_make is set to false. can_make is the return value of the
    #method.
    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    #The instance method make_drink has one attribute other than self and this is order. The for loop uses
    #drink.ingredients which essentially uses the drink instance attribute combined with the list of ingredients
    #form the MenuItem class to tell the for loop how many times to run in this case it will be three as there are
    #three ingredients (water, ice and orange). It takes the amount of an each ingredient from self.resources and subtracts
    #the amount of ingredient used to make the drink.
    def make_drink(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} orange juice. Enjoy!")