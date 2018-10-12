#Python vending machine - 22/02/17

class Machine: #make vending machine object
    def __init__(self):
        self.balance = 300 #set balance
        self.items = [] #set items / inventory
        self.menu() #call menu procedure
    
    def menu(self):
        print("""
[1]Buy Items
[2]View Balance
[3]View Items
[4]Quit
    """) #print a menu 
        choice = input("Enter your choice: ") #offer the user some input to select what they want to do
        if choice == '1': #if they select option number 1
            self.buy_items() #direct them to the buy items procedure
        elif choice == '2': #if they select option number 2
            print(self.balance,'p') #display their balance
            self.menu() #direct back to menu
        elif choice == '3': #if they select option number 3
            print(''.join([x + '\n' for x in self.items])) #display the inventory
            #that line takes every item in the array and calls it 'x', it then prints each 'x' with a new line
            self.menu() #direct to menu
        elif choice == '4': #if they select option number 4
            quit() #quit the program

    def buy_items(self):
        print("""
[1]Crisps - 50p
[2]Coke - £1.20
[3]Protein Bar - £90p
    """) #display options
        choice = input(">> ") #input for options
        if choice == '1': #if they chose 1
            if self.balance >= 50: #check to see if they have enough money
                self.balance -= 50 #if they do, subtract the cost from their balance
                self.items.append("Crisps") #add crisps to inventory
                print("Bought 1x Crips for 50p!") #tell user they bought crisps
                self.menu() #direct to menu
            else: #if they don't have enough money
                print("Not enough money to buy crisps") #print an error message
                self.menu() #direct back to menu
        elif choice == '2': #if they chose 2
            if self.balance >= 120: #check to see if they have enough money
                self.balance -= 120 #if they do, subtract the cost from their balance
                self.items.append("Coke") #add coke to inventory
                print("Bought 1x Coke for £1.20") #print message
                self.menu() #you get the idea....
            else:
                print("Not enough money to buy coke")
                self.menu()
        elif choice == '3':
            if self.balance >= 90:
                self.balance -= 90
                self.items.append("Protein Bar")
                print("Bought 1x protein bar for 90p")
                self.menu()
            else:
                print("Not enough money to buy protein bar")
                self.menu()
        else:
            print("Not a valid option")
            self.menu()

if __name__ == '__main__': #if the app is being run directly. IE not being
    #run through a module (like when you do import random or import os)
    machine = Machine() #create the machine
    


            
        
        
