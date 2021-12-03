import time, sys, random, colorama
from colorama import Fore, Style
colorama.init (autoreset=True)
typing_speed = 50 

def pause(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*6.0/typing_speed)

def pauseNext(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

def getCount():
    pause("\nWelcome to Input Counter 2.0! To proceed, please enter a sentence.\n")
    userInput = input()
    vowels = 0
    consonants = 0
    res = len(userInput.split())
    for i in str.casefold(userInput):
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowels += 1
        elif i == " " or i == "." or i == "!" or i == "?" or i == ",":
            consonants == 0
        else:
            consonants += 1
    pauseNext(f'\nYour original input is "{userInput}"\n')
    time.sleep(1)
    print("\nThe number of" + Fore.YELLOW + " words " + Style.RESET_ALL + "in your input is:", Fore.YELLOW + str(res))
    time.sleep(1)
    print("The number of" + Fore.CYAN + " vowels " + Style.RESET_ALL + "in your input is: " + Fore.CYAN + str(vowels))
    time.sleep(1)
    print("The number of" + Fore.GREEN + " consonants " + Style.RESET_ALL + "in your input is: " + Fore.GREEN + str(consonants))
    time.sleep(1)
    pauseNext("\nThank you for using Input Counter 2.0! Hope to see you again, iskolar ng bayan!\n")

getCount()