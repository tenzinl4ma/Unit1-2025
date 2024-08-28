import sys
import time

print("Welcome!.")
#
time.sleep(1)
def find_factor(number):
    factor=[]
    for i in range(1,number):
        if number % i ==0:
            factor.append(i)
    return factor
numbers=[21,55,10,90,6]
for num in numbers:
    factor=find_factor(num)
    print(f"The factors of the {num}: {', ' .join(map(str, factor))}")


def is_perfect_num(number):
    factor= find_factor(number)
    return sum(factor)==6
ask=input(" Do you want to check if 6 is a perfect number or not? Y/N \n>>>")

if ask.lower()=="y":
    print("wait! let me think for sec.")
    print("loading")
    time.sleep(1)
    print("loading.")
    time.sleep(1)
    print("loading..")
    time.sleep(1)
    print("loading...")
    time.sleep(1)
    print("Yes, Its perfect number.")
    time.sleep(1)
    print(f"The factors of 6: {', '.join(map(str,factor))} True")
elif ask.lower()=="n":
    print("So, sad")
    time.sleep(2)
    print("                    <<< See You Soon! >>>")
    sys.exit()
else:
    print("so frustrating")
    time.sleep(2)
    print("Why don't you listen to my instructions! ")