# This is the random password generator

### you can choose to include the special char or not
### I have included time to create more realiastic and if user ask for length of 20 char password will be in red and have add password length strenth and limitation.

## Flowchart



## question 

<img width="1170" alt="Screenshot 2024-09-09 at 13 12 16" src="https://github.com/user-attachments/assets/987d5bd8-635c-4b39-b713-e9ee62aec763">


## Code
```.py
import sys
import time
import random


def generator():
    ask = input("Do you want special characters in the password? (Yes/No): ").lower()

    if ask == 'yes':
        all_chars = pas + specialchar
        password = [str(random.choice(all_chars)) for _ in range(password_length)]
    else:
        password = [str(random.choice(pas)) for _ in range(password_length)]

    password_str = ''.join(password)
    if password_length==20:

        print(f"Your password is: \033[0;31m{password_str}\033[0m")
    else:
        print(f" your password is: {password_str}")


print("This is the password generator")
time.sleep(1)


pas = [1, 2, 3, 4, 5, 6, 7, 8, 9,
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

specialchar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
password_length = int(input("Enter the password length: "))


if password_length < 8:
    print("Password is too short! It must be at least 8 characters long.")
    sys.exit()  # Exit
elif password_length > 20:
    print("Password is too long! Maximum allowed length is 20.")
    sys.exit()
else:
    print("Generating your password...")
    time.sleep(2)
    generator()


```


## Proof

<img width="1680" alt="Screenshot 2024-09-09 at 13 54 55" src="https://github.com/user-attachments/assets/f00570d8-e470-48e3-96be-e0d111b06605">

