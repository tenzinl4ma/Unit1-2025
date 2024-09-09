'''
x= int(input(" enter 1 for odd and 2 for even:"))
n=int(input("enter the num till you want even:"))

even= list(range(x,n,2))
print(even)

# program to create table of multiplication
for i in range(1,10):
    multiply=[value*i for value in range(1,11)]
    print(multiply)

cars= ['audi','bmw','supra']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.capitalize())

a= 'mushroom'
if a !='toping':
    print("hold this topping")
#num guess
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
            print("num too low")
        else:
             print("invalid number")
guesser(x)'''
