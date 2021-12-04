import time, sys, random
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

def greetUser():
    pauseNext("\nWelcome to Password Validator!")
    time.sleep(2)
    print("\nTo ensure the validity of your password, please make sure to meet the following criteria:\n")
    time.sleep(2)
    pause("Password must be greater than 15 characters.\n")
    time.sleep(.5)
    pause("Password must contain at least one number.\n")
    time.sleep(.5)
    pause("Password must contain at least one capital letter.\n")
    time.sleep(.5)
    pause("Password must contain at least one special character.\n")
    time.sleep(1)

def checkPassword():
    criteria = {
        "number" : "[0123456789]",
        "capital letter" : "[ABCDEFGHIJKLMNOPQRSTUVWXYZ]",
        "special character" : """[!#$%&"'()*+,-./:;<=>[]?@\^_{|}~]""",
    }
    checkCriteria = 0
    userInput = ''
    while len(userInput) < 15 or checkCriteria != 3:
        userInput = input("\nEnter new password: ")
        checkCriteria = 0
        for nameCriterion, criterion in criteria.items():
            pauseNext(f"\nChecking {nameCriterion}...\n")
            valid = [ch for ch in criterion if ch in userInput]
            if valid: 
                checkCriteria += 1
            else:
                time.sleep(.5)
                print(f"Your password must contain at least one {nameCriterion}.")
                time.sleep(.5)
        if checkCriteria == 3:
            time.sleep(1)
            print ("\nPassword is valid. You may proceed.")
            time.sleep(1)
        else:
            time.sleep(1) 
            print("\nPassword is invalid. Please try again.")   

greetUser()
checkPassword()