from validation import color
import random
x= random.randint(4,10)
import sys
def guesser(x):
    while True:
        guess=int(input("guess the number:"))
        if guess == x:
            print("you are right")
            sys.exit()
        elif guess>x:
             print("num too high")
        elif guess<x:
            print(f"{color.fg.red}num too low{color.reset}")
        else:
             print(f"{color.fg.red}invalid number")
guesser(x)