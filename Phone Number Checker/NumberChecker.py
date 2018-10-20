#20/11/2016

import string
valid = string.digits
count = 0

while True:
        number = str(input("Type number here: ")) 
        for x in number:
            if x not in valid:
                count += 1
                if count > 0:
                    print("[*]Numbers only please")
                    break
        if number[0] != "0":
            print("[*]Doesn't start with 0")
        if number[1] == "0":
            print("[*]2nd number can't be 0")
        if len(number) < 11:
            print("[*]You need",11-len(number),"More Characters for it too be valid")
        if len(number) > 11:
            print("[*]too many characters")
        if len(number) == 11:
            print("It's valid")
            
