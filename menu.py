#This class provides the blueprint that is used to define each individual item on the menu in the Menu class. it models each menu item
#Each object that is created from this MenuItem class will have five instance attributes
#(name, ice, water, orange and cost).
class MenuItem:
    def __init__(self, name, ice, water, orange, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "ice": ice,
            "water": water,
            "orange": orange
        }


#This class uses the MenuItem class to define a menu. It models the menu with strength of drinks.
#The MenuItem class is called three times to create three MenuItem objects.
#Each MenuItem object forms part of the list which defines the self.menu instance attribute.
class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="strong", ice=20, water=10, orange=40, cost=1),
            MenuItem(name="medium", ice=30, water=20, orange=30, cost=0.5),
            MenuItem(name="weak", ice=40, water=30, orange=20, cost=0.25),
        ]

    #This instance method returns all the name sof the available drinks. Options is set to an empty string and a for loop
    #is used to iterate through the self.menu list which is an instance variable in the init method of the Menu class.
    #the name of each menu item is appended to the options empty string with a "/" separating each item. The options
    #string is returned
    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    #Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None.
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

