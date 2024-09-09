import random
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"#$%&'
random_string = ' '
passworlength=int(input("choose the length of the password"))
for i in range (passworlength):
    randomchar=random.choice(alphabet)
    random_string+=randomchar
redcolor="\033[91m"
greencolor="\033[92m"
print(greencolor+ "Below is the generated password")
print("["+redcolor+random_string+ "\033[0m"+" ]")