import random
import sqlite3
import logging

#Logging Configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s:')
file_handler = logging.FileHandler('databaselog.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)+
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
"""USE logger.info('MESSAGE') TO CREATE LOG STATEMENT"""

##cursor.execute('''
##    CREATE TABLE users(name TEXT, score INTEGER,
##                       id INTEGER PRIMARY KEY)
##''')
##cursor.execute("DROP TABLE users")

class Login:
    START = 1
    #This is for when we do global()[var stuff] because the function is called twice, and if I don't do this then the first variable
    #will be called 'player1' and then the next one will be called 'player1' as well and will overwrite the first one.
    def __init__(self):
        pass
        
    def add(self,name):
        _id = random.randint(1,100) #Generates random ID number
        try: #Try and add user to database
            cursor.execute('''INSERT INTO users(name,score,id)
                              VALUES(?,?,?)''',(name.lower(), 0, _id))
            conn.commit()
        except sqlite3.IntegrityError: #If the unique ID which is generated is used then just try again, on a range of 400+ this is unlikely to happen unless here are a large amount of users
            self.add(name) #try again with the same name entered first and generate new 
        
    def try_login(self, name):
        cursor.execute("SELECT * FROM users WHERE name = '{}'".format(name.lower())) #Get entered user's data.
        rows = cursor.fetchall() #cursor.fetchall() gets the data from the above SQL statement
        if len(rows) == 0: #If no data is found
            print("No user found under the name of {}.\nWould you like to be added to the database? [Y/N]: ".format(name));choice = input(">> ")
            if choice.lower() == 'y':
                self.add(name) #Create player in database
                cursor.execute("SELECT * FROM users WHERE name = '{}'".format(name.lower())) #get data of added user (default data set in add())
                rows = cursor.fetchall() #stores as a var
                self.setter(name, rows) #makes a variable of the instance
            else: #if they press no
                print("Okay, please re-enter player's name.")
                main()
        else: #If they're found
            self.setter(name, rows) #make var

    def setter(self, name, rows):
        p = Player(name, rows) #makes a instance of player
        game.addPlayer(p) #calls addPlayer
        for i in range(self.START,len(game.players)+1): #1 - however many players exist
            globals()["player{}".format(i)] = p #make a varaible called 'player + i' so: player1, player2, player3 etc..
            self.START += 1

class Player:
    def __init__(self, name, rows):
        self.name = name
        self.score = rows[0][1] #Indexing gets score 
        self.id = rows[0][2] #Indexing gets ID

    def addScore(self, increment):
        self.score += increment


class Game:
    def __init__(self, _range=6): #If _range not defined then default is 6
        self.range = _range
        self.players = []

    def addPlayer(self, player): #Takes the object of the player
        #attribs = [a for a in dir(player) if not a.startswith('__') and not callable(getattr(player,a))]
        attributes = [player.name, player.score, player.id] #gets attributes of the player
        self.players.append(attributes) #adds to game list

    def rollDice(self):
        player1dice =  (random.randint(0,self.range),random.randint(0,self.range)) #Generate 2 nums for p1 
        player2dice =  (random.randint(0,self.range),random.randint(0,self.range)) #Generate 2 nums for p2
        print(f"{player1.name} - {player1dice[0:]}")
        print(f"{player2.name} - {player2dice[0:]}")
        if player1dice[0] == self.range and player1dice[1] == self.range and player2dice[0] == self.range and player2dice[1] == self.range:
            print("It's a draw!")
            logger.info("{} just drew with {}".format(player1.name, player2.name))
        elif player1dice[0] == self.range and player1dice[1] == self.range:
            print("{} Wins!".format(player1.name))
            logger.info("{} just beat {}".format(player1.name, player2.name))
            self.winner = player1
            self.retry()
        elif player2dice[0] == self.range and player2dice[1] == self.range:
            print("{} Wins!".format(player2.name))
            logger.info("{} just beat {}".format(player2.name, player1.name))
            self.winner = player2
            self.retry()

    def retry(self):
        retry = input("Would you like to save scores and exit? [Q]\nOr play again [R]: \n>>")
        if retry.lower() == 'r':
            Login.start = 1
            main_menu()
        else:
            self.winner.score += 1
            cursor.execute("UPDATE users SET score='{}' WHERE name ='{}'".format(int(self.winner.score), self.winner.name)) #update score value
            conn.commit() #save
            quit()
            
game = Game(6)
login = Login()

def CreateMenu(choices):
    def menu_wrapper(func):
        def inner(*args, **kwargs):
            menu = '\n'
            for index, option in enumerate(choices):
                menu += f'{index + 1}) {option}\n'
            menu += '99) Back\n'
            print(menu)
            while True:
                choice = input('[*] Please Enter Your Choice: ')
                try:
                    choice = int(choice)
                    if not (choice >= 1 and choice <= len(choices)):
                        print('\n[!] That\'s Not A Valid Choice!')
                        print(menu)
                    else:
                        return func(choice)
                except ValueError:
                    print('\n[!] Enter An Integer Please!\n')
                    
        return inner
    return menu_wrapper


def viewScores(rows):
    score_const = 16
    print("""
======       =======       ====
=NAME=       =SCORE=       =ID=
======       =======       ====
""", end="", flush=True)
    for x in range(0,len(rows)):
        if len(rows[x][0]) > 6:
            print(rows[x][0][0:6]+"...", end=(score_const-9) * " ", flush=True)
            print(rows[x][1], end=11*" ", flush=True)
            print(rows[x][2])
        else:
            print(rows[x][0][0:6], end=(score_const-len(rows[x][0])) * " ", flush=True)
            print(rows[x][1], end=11*" ", flush=True)
            print(rows[x][2])

def manageUsers(rows):
    index = None
    #get index and if found update index variable
    choice = input(">> ")
    for x in range(0, len(rows)+1):
        if choice in rows[x]:
            index = rows[x].index(choice)
            print(rows[index])
            break
        else:
            print("no")
            




@CreateMenu(["Play A Game", "View Scores", "Manage Users"])
def main_menu(choice):
    login = Login()
    game.players = []
    if choice == 1:
        p1 = input("Player 1's name: ")
        login.try_login(p1)
        p2 = input("Player 2's name: ")
        login.try_login(p2)
        while True:
            input("Press enter >> ")
            game.rollDice()
          
    elif choice == 2:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        viewScores(rows)

          
    elif choice == 3:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        manageUsers(rows)

    elif choice == 99:
        exit()

main_menu()

##def main():
##    game.players = []
##    login = Login()
##    p1 = input("Player 1's name: ")
##    login.try_login(p1)
##    p2 = input("Player 2's name: ")
##    login.try_login(p2)
##    print("Welcome {} and {} to the game".format(p1, p2))
##    while True:
##        input("Press enter >> ")
##        game.rollDice()
##if __name__ == '__main__':
##    main()

                          
