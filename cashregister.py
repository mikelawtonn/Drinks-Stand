#This class has a class variable CURRENCY which is set equal to the string "£" and another class variable COIN_VALUES
#which is set equal to a set a dictionary deifned by key-value pairs of money corresponding to the amount the money is
#worth
class CashRegister:

    CURRENCY = "£"

    COIN_VALUES = {
        "20p": 0.20,
        "10p": 0.10,
        "5p": 0.05,
        "1p": 0.01
    }

    #The initialization method sets self.profit and self.money_received both equal to 0.
    def __init__(self):
        self.profit = 0
        self.money_received = 0

    #Prints the current profit by using string formatting to insert "£" for self.CURRENCY and whatever the current
    #profit is for self.profit.
    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    #Prints a statement to screen asking the user to insert coins. For loop that iterates through the values in the
    #class attribute COIN_VALUES and uses an input variable that akss the user how many coins of that particular value they have then multiplies
    #the value of the coins by the number of coins and adds this to money-received insatnce attribute. Essentially,
    #returns the total calculated from coins inserted.
    def process_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    #This instance method calls the process_coins instead method using self.process_coins(). There is an if statement that states that if
    #money_received (which is calculated in process_coins method) is greater than or equal to cost then change will be set equal to
    #money_received subtract cost and rounded to 2 decimal places. A print statement that uses a formatted string is then used to print
    #amount of change to screen. The cost is then added to profit and money_received is reset to 0. Also if self.money_received >= cost then
    #the if statement returns True. If self.money_received is not >= cost then the statement returns False.
    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False