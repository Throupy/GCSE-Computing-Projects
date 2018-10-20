#29/01/2017

while True:
    word = input("Enter a word: ")
    if str(word) == str(word)[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
