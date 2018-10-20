domains = ["gmail", "hotmail", "yahoo", "icloud"]
endings = ["com", "co.uk", "org"]

def emailCheck(email):
    for letter in email:
        if letter == '@':
            if email[email.index(letter)+1:].split(".",1)[0] in domains:
                if email[email.index(letter)+1:].split(".",1)[1] in endings:
                    return True


while True:
    email = input('>> Enter email: ')
    if emailCheck(email):
        print(f"'{email}' is valid!")
    else:
        print(f"'{email}' is invalid!")


