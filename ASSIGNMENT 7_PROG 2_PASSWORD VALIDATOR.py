import time, sys, random, colorama
from colorama import Fore, Style
colorama.init (autoreset=True)
typing_speed = 50

def pause(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*4.0/typing_speed)

def pauseNext(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

def checkPassword():
    userInput = input("\nEnter your password: ")
    print("\n")
    numbers = "[0123456789]"
    uppercase = "[ABCDEFGHIJKLMNOPQRSTUVWXYZ]"
    specialChars = "[!#$%&()*+,-./:;<=>[]?@\^_{|}~]"
    criteria = 0; x = 0; y = 0; z = 0
    while criteria != 3:
        while len(userInput) < 15:
            print("Your password must be greater than 15 characters.")
            break
        if not any(char in numbers for char in userInput):
            print("Your password must contain at least one number.")
            break
        elif not any(char in uppercase for char in userInput):
            print("Password must contain at least one uppercase letter.")
            break
        elif not any(char in specialChars for char in userInput):
            print("Password must contain at least one special character.")
            break

        for i in range(len(userInput)):
            if userInput[i] in numbers:
                x = 1
            elif userInput[i] in uppercase:
                y = 1
            elif userInput[i] in specialChars:
                z = 1
            criteria = x + y + z
    if criteria != 3:
        print("\nPassword is invalid. Please try again. ")
        return False
    else:
        print("Password is valid. You may proceed.")
        return True
        
valid = False
while not valid:
    valid = checkPassword()

