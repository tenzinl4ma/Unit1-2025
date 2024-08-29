## password generator from provided list
##you can choose your own length
import sys
import time
import random
# create function to generate random string
def generator():
    password = [str(random.choice(pas)) for _ in range(password_length)]
    password_str = ''.join(password)#join and store the random num
    print("Your password can be:", password_str)


print(" This is the password generator")
time.sleep(1)


pas= [1,2,3,4,5,6,7,8,9,"x","y","$","!"]
password_length = int(input("Enter password length: "))
if password_length < 8:
    print("Password not strong!")
    sys.exit()
elif password_length > 20:
    print("Password too long!")
elif password_length > 8 or password_length==8:
    print("Wait let me think")
    print("Loading.")
    time.sleep(2)
    print("Loading..")
    time.sleep(2)
    print("Loading...")
    time.sleep(2)
    print("Gotcha")
    generator()

