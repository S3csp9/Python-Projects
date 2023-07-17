import string
import random

while True:
    passchar = ""
    password = []
    
    print("\nDo you want to Start the Program ? \n1. Start \n2. Exit")
    inpo = int(input("Choose Option : "))
    
    if inpo == 1:
        long = int(input("Enter Password Length : "))
        print("What thing you want to add in your Password ? \n1. Letters \n2. Digits \n3. Special Characters \n4. Letters+Digits \n5. All")
        inp = int(input("Choose Option : "))
        
        if inp == 1:
            passchar += string.ascii_letters
            for i in range(long):
                word = random.choice(passchar)
                password.append(word)
            print("Your Password : "+"".join(password))
        elif inp == 2:
            passchar += string.digits
            for i in range(long):
                word = random.choice(passchar)
                password.append(word)
            print("Your Password : "+"".join(password))
        elif inp == 3:
            passchar += string.punctuation
            for i in range(long):
                word = random.choice(passchar)
                password.append(word)
            print("Your Password : "+"".join(password))
        elif inp == 4:
            passchar += string.ascii_letters
            passchar += string.digits
            for i in range(long):
                word = random.choice(passchar)
                password.append(word)
            print("Your Password : "+"".join(password))
        elif inp == 5:
            passchar += string.ascii_letters
            passchar += string.digits
            passchar += string.punctuation
            for i in range(long):
                word = random.choice(passchar)
                password.append(word)
            print("Your Password : "+"".join(password))
        else:
            print("Choose a Valid Option.")
            
    elif inpo == 2:
        quit()
    else:
        print("Choose a Valid Option.")