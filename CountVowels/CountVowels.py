#02/02/2018
import string
import time

vowels = ['a','e','i','o','u']

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.vowels = 0
        self.words = 0
        self.upper = 0
        self.lower = 0
        self.chars = 0
        self.digits = 0

    def countVowels(self):
        """Counts Vowels"""
        for letter in self.sentence:
            if letter.lower() in vowels:
                self.vowels += 1

    def countWords(self):
        """Counts words"""
        self.words += len(self.sentence.split(" "))

    def countAll(self):
        """Counts vowels, upper case, lower case, digits, characters and whitespace"""
        self.words += len(self.sentence.split(" "))
        for letter in self.sentence:
            if letter.lower() in vowels:
                self.vowels += 1
            if letter in string.ascii_lowercase:
                self.lower += 1
                self.chars += 1
            if letter in string.ascii_uppercase:
                self.upper += 1
                self.chars += 1
            if letter in string.digits:
                self.digits += 1
                self.chars += 1
            if letter in string.whitespace:
                self.chars += 1


#This menu system does not belong to me.
#All credit to https://github.com/Bentechy66
def CreateMenu(choices):
    def menu_wrapper(func):
        def inner(*args, **kwargs):
            menu = '\n'
            for index, option in enumerate(choices):
                menu += f'[-] {index + 1}) {option}\n'

            menu += '[-] 99) Back\n'
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


@CreateMenu(["Count all vowels", "Count all words", "Count everything"])
def main_menu(choice):
    if choice == 1:
        sentence = input("Enter a sentence: ")
        sentence = Sentence(sentence)
        sentence.countVowels()
        print(sentence.vowels)
      
    elif choice == 2:
        sentence = input("Enter a sentence: ")
        sentence = Sentence(sentence)
        sentence.countWords()
        print(sentence.words)

    elif choice == 3:
        sentence = input("Enter a sentence: ")
        sentence = Sentence(sentence)
        sentence.countAll()
        print(f"{sentence.sentence} has \n{sentence.vowels} Vowels\n{sentence.words} Words\n{sentence.upper} Upper Case\n{sentence.lower} Lower Case\n{sentence.chars} Characters\n{sentence.digits} Digits")

    elif choice == 99:
        exit()

while True:
    time.sleep(1)
    main_menu()






    
