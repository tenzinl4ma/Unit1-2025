<h1 align="center" >Todo List</h1> 

# Criteria A: Planning

## Problem definition

My client, is a young social media influencer who take a lots of the photos and post in many social media platform like Tiktok, Instagram and Facebook. He start his passion since he was middle school student and till these days his passion has never faded. He wanted to be a great influencer and has wide friend zone where they share a lots of thing, but the problem is they also share the phone with eachother, even though he trust his friend 100%, he doesn't trust the situation upcoming. We never know what will happen coming days, so he want a product that manage all social media and important passwords that is  well hidden like in vault that doesn't look like a password managers and, no unathorised person could access it.

There is no such existing product that meets my clients requirement, allowing him to store and manage his password well hidden. So, is in need of someone who is capable of developing such app that fulfill his requirments. A developer myself, agrees to develop a product that meets his requirements, allowing him to manage and store the password of his social media account that is well hidden behind other app.

Moreover he is open to any additional function or customization that developer will add.

## Proposed solution

Design statement: I will create a **To-do list app** for my client it will be an **simple terminal application that can only access and run through terminal** and will be developed by **PyCharm** code editor. It will take **two weeks** to finish and will be evaluated according to the criteria **A, B, and C**.

### Introduction to the Encryption: 
In this product developmet process the encryption is very important to know for both developer and client side. Encryption is the method of securing your data and information into some other form that is unable to read and understand by the intercepter until its decrypted with corrected code. People often have misconception of believing that encryption and password is same, but ther is huge difference between them is that password is plain text if someone know it they can use it to access but encryption is a encoded form that even one know it they won't be able to use it till they decrypt it.


## Design Statement(rationale):
The product will be developed on the popular python Integrated Development Environment called PyCharm software which is developed by Czech company Jetbrain which has wide range of essential tools that helps developers to cuztomize and add the desired functions. I also has lots of plug-in and shortcuts which enables developer's to developed efficiently providing developer friendly environment. This IDE best fit for the developer to achieve the goals that the client has set and shorten the time compare to other software.

Some important features of this product include: a terminal based interface to-do list application that is capable of adding the multiple tasks, viewing the text and removing the tasks, it also shows the user friendly error message 'invalid input' if input is incorrect. It function as normal to-do list. It provide a warm and user friendly welcome message and also accept a **secret code** from user, if secret code is input, it will ask for password. If the user input the incorrect password for thrice the system will no longer take the keyboard and mouse input, completly locking the system till you swap the window. However the user input correct password it will show all the encrypted password in decrypt form. After, entering the password file you can add, delete the password list. All these function and completed app frame provide and fulfill the clients demands.


## Success criteria

1. The To-do list is a text-based software (Runs in the Terminal).

2. The To-do list is capable of adding, viewing and removing the tasks smoothly.

3. The To-do list shows user friendly message when doing the operation .

4. The To-do list accept secretcode and password from user and direct them to the password manager.

5. It shows error message or play sound when you input password.

7. The password saved in tsv.file is encrypted form and will be decrypt when its open through password manager.

6. In password manager you can retrive, add, remove the password which will also changes will take place in original file.



# Criteria B: Design

#### System Details

<img align="left" width="445" alt="Screenshot 2024-09-23 at 23 17 33" src="https://github.com/user-attachments/assets/0b04e11a-1c14-4ad3-85f7-7639bd9ecf40">

### The system details
##### **pwd** shows the current working directory and <br>**ls -l** shows the list of all the files inside that directory <br>with the date modified <br>**python3 --version** show the version of python installed in <br>system and the **system_profiler SPHardwareDataType**<br> shows the system software details.<br clear="left"/>
----------------------------------------------------------------------------------------------------------------------------------------

## **Fig-1** The System Diagram

<img width="900" align="center" alt="System diagram" src="https://github.com/user-attachments/assets/bf0aba54-4440-46a9-81dc-2dacc89b3446">






## Flow diagrams












## Record of tasks
| Task Number | Planned Action                                            | Planned Outcome                                                              | Time estimated | target completion date | Criterion |
|-------------|-----------------------------------------------------------|------------------------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | 1st meeting with client                                   | obtain a problem defination understand the situation                         | 10 min         | sep 7                  | A         |
| 2           | Brain-storm and propose  solution                         | jot down the ideas and  solution                                             | 25 min         | sep 8                  | A         |
| 3           | choose the system and IDE                                 | To choose the best fit hard- ware and software for deve- loping the products | 15 min         | sep 10                 | A         |
| 4           | flowchart and diagram for To-do list and encrypted  files | To create the best solution                                                  | 30 min         | sept 12                | B         |
| 5           | Alpha Development                                         | Code first draft of the program that meets client demands                    | 12 hrs         | sept 15                | C         |
| 6           | Beta Testing                                              | Trace and find the bugs, errors, by testing with users                       | 2 hrs          | sept 18                | A         |
| 7           | Beta Development                                          | Fix the bugs, errors and  add more functionalities.                          | 9 hrs          | sept 20                | C         |

## Test Plan
| Test  No | Test Type        | User Input       | Expected  Output                       | Testing Status Pass/Fail | Related  success Criteria                             |
|----------|------------------|------------------|----------------------------------------|--------------------------|-------------------------------------------------------|
| 1        | welcome  message | NONE             | Welcome to Todo-list                   | Pass                     | shows  messages                                       |
| 2        | ask for input    | add/view/remove  | type add/view /remove                  | Pass                     | able to add, view or remove the list                  |
| 3        | secret code      | sudouser         | opening  credential                    | Pass                     | open the tsv file                                     |
| 4        | wrong password   | invalid input    | lock hardware input and show gif image | Pass                     | after 3 attempts of of the password shows gif         |
| 5        | encrypt file     | cd important.tsv | password list in tsv file              | Pass                     | encrypt the file in  reverse                          |
| 6        | decrypt file     | cd program001.py | shows the file in  decrypt             | Pass                     | the tsv file is reverse again to decrypt the  message |
# Criteria C: Development

python starter 
```.py
from time import sleep

from gifpass import open_gif, welcomemsg, passwordmanagers,todo_list
import time
sleep(0.01)
welcomemsg()
todo_list()
  

```
main code


```.py


import time
from validation import color
import datetime
import getpass
from secretvault import secretvault
import sys
import pygame
def audio_player(audio_file):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(audio_file)

    # Play the audio
    pygame.mixer.music.play()

    # Keep the program running while the audio is playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def open_gif():
    print(color.fg.red+r'''
 ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░▒▓███████▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓██████▓▒░       ░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░       
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░▒▓███████▓▒░       ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░ 
    ''')
    sleep(3)
    print("Your permission has been denied!"+color.reset_all)
    sleep(3)



from time import sleep

from validation import color
def welcomemsg():
    print("""

    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██╗    ████████╗ ██████╗     ████████╗██╗  ██╗███████╗
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝██║    ╚══██╔══╝██╔═══██╗    ╚══██╔══╝██║  ██║██╔════╝
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ██║       ██║   ██║   ██║       ██║   ███████║█████╗  
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝       ██║   ██║   ██║       ██║   ██╔══██║██╔══╝  
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗██╗       ██║   ╚██████╔╝       ██║   ██║  ██║███████╗
     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝       ╚═╝    ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝

        """)
    sleep(1)
    print(color.fg.yellow+"""   
                        ████████╗ ██████╗     ██████╗  ██████╗     ██╗     ██╗███████╗████████╗██╗
                        ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔═══██╗    ██║     ██║██╔════╝╚══██╔══╝██║
                           ██║   ██║   ██║    ██║  ██║██║   ██║    ██║     ██║███████╗   ██║   ██║
                           ██║   ██║   ██║    ██║  ██║██║   ██║    ██║     ██║╚════██║   ██║   ╚═╝
                           ██║   ╚██████╔╝    ██████╔╝╚██████╔╝    ███████╗██║███████║   ██║   ██╗
                           ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝     ╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝




          """+color.reset)
    sleep(0.5)
def passwordmanagers():
    print("                                Opening the secret Cretentials.")
    sleep(1)
    print("                                Opening the secret Cretentials..")
    sleep(0.2)
    print("                                Opening the secret Cretentials...")
    sleep(0.2)
    print("                                Opening the secret Cretentials....")
    sleep(0.2)
    correct_password = "tenzin123"
    attempts = 0
    if attempts>=2:
        open_gif()
    while attempts < 3:
        password = getpass.getpass("You need to input the password: ")
        if password == correct_password:
            audio_player('/Users/m22-007/PycharmProjects/unit1-2025/Project/Y2meta.app - Access Granted Sound (128 kbps).mp3')
            print(color.fg.red+r'''
   _   ___ ___ ___ ___ ___    ___ ___    _   _  _ _____ ___ ___  
  /_\ / __/ __| __/ __/ __|  / __| _ \  /_\ | \| |_   _| __|   \ 
 / _ \ (_| (__| _|\__ \__ \ | (_ |   / / _ \| .` | | | | _|| |) |
/_/ \_\___\___|___|___/___/  \___|_|_\/_/ \_\_|\_| |_| |___|___/ 
            ''',color.reset_all)
            while True:
                secretvault()



now = datetime.datetime.now()
secretcode = f"{now.hour:02}{now.minute:02}"
code=str(secretcode)
print(code)
def todo_list():
    tasks = []
    print("\r   \033[1m           This is a simple to do list \U0001f600", end='', flush=True)
    while True:
        action = input(color.reset+"Choose an action: [a for add/v for view/r for remove/q for quit]: ").strip().lower()
        if action==code:
            passwordmanagers()
        if action == 'add' or action== 'a':
            print("Input your all task and press e for exit")
            while True:
                task = input("Enter a task: ")
                if task=="exit" or task=="e":
                    break
                current_hour, current_minute = datetime.datetime.now().hour, datetime.datetime.now().minute
                tasks.append(f"{task} (added on {current_hour} o'clock {current_minute} minute)")
                print(f"Task added: {task} at {current_hour}:{current_minute}")

        elif action == 'view' or action=='v':
            if not tasks:
                print("There is no task added yet.")
            else:
                print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif action == 'remove' or action=='r':
            print("input 0 to go back.")
            while True:
                print("\nTo-Do List:")
                for i, task in enumerate(tasks, start=1):

                    print(f"{i}. {task}")

                user_input = input("\nEnter task number to remove or type 'done' to exit: ")

                if user_input.lower() == 'done':  # If the user types 'done', exit the loop
                    print("Exiting...")
                    break
                if user_input.lower() =='new' or user_input.lower()=="n":
                    print("Fresh Page")
                    tasks.clear()
                    break

                try:
                    task_num = int(user_input) - 1  # Convert input to an index number

                    if 0 <= task_num < len(tasks):

                        removed_task = tasks.pop(task_num)
                        print(color.fg.red,f"Removed task: {strike_through(removed_task)}",color.reset_all)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number or type 'done' to exit.")


        elif action == 'quit':
                print("Goodbye!")
                break
        else:
            print("Invalid action.")
#




def strike_through(text):
    return f'\033[9m{text}\033[0m'


```



## password manager code


```.py

import colorama as color
from time import sleep
import random
import string
import sys



def secretvault():
    while True:
        # Read all lines from the TSV file
        lines = open("importantdoc.tsv", "r").readlines()

        # Display the tasks with passwords hidden as asterisks
        print("Current Password List:")
        for i, line in enumerate(lines, start=1):
            parts = line.strip().split('\t')  # Split the line into parts
            if len(parts) == 3:
                password, account_id, account_name = parts
                hidden_password = '*' * len(password)  # Replace password with asterisks
                print(color.Fore.RED, f"{i}. {account_name} - {hidden_password} (ID: {account_id})",
                      color.Style.RESET_ALL)

        # Menu for user actions
        ask = input("Choose: [a for add / r for remove / q for quit / v for view password]: ").strip().lower()


        if ask == "q":
            break
        elif ask == "a":
            passs=input("do you want to generate the password:")
            if passs=="y":
                length = input("Enter password length (8-20): ")

                if not length.isdigit() or not (8 <= int(length) <= 20):
                    print("Length must be between 8 and 20.")

                length = int(length)
                sleep(1)  # Simulate delay
                chars = string.ascii_lowercase + string.digits + (
                    string.punctuation if input("Include special characters? (y/n): ").lower() in ['y', 'yes'] else '')

                password = ''.join(random.choice(chars) for _ in range(length))

                print(f"Your password is: {password}")
                new_account_id = input("Enter account ID: ")
                new_account_name = input("Enter account name: ")
                # Append the new entry, reversed
                new_entry = f"{password[::-1]}\t{new_account_id}\t{new_account_name[::-1]}\n"
                open("importantdoc.tsv", "a").write(new_entry)
            if passs=="n":
                new_password = input("Enter new password: ")
                new_account_id = input("Enter account ID: ")
                new_account_name = input("Enter account name: ")
                # Append the new entry, reversed
                new_entry = f"{new_password[::-1]}\t{new_account_id}\t{new_account_name[::-1]}\n"
                open("importantdoc.tsv", "a").write(new_entry)
        elif ask == "r":  # Removing an entry
            line_to_remove = int(input("Enter line number to delete: "))
            if line_to_remove == 1:
                print("You are not allowed to delete the Header of the list")
            elif 2 <= line_to_remove <= len(lines):
                del lines[line_to_remove - 1]
                open("importantdoc.tsv", "w").writelines(lines)
        elif ask == "v":  # Viewing a password
            line_to_view = int(input("Enter line number to view password: "))
            if 1 <= line_to_view <= len(lines):
                chosen_line = lines[line_to_view - 1].strip()  # Get the chosen line
                parts = chosen_line.split('\t')
                if len(parts) == 3:
                    password, account_id, account_name = parts
                    print(color.Back.RED,f"Password for {account_name} (ID: {account_id}) is: {password[::-1]}",color.Back.RESET)
                else:
                    print("Invalid entry format.")
            else:
                print("Invalid line number.")
        else:
            print("Invalid option, please read the instructions clearly.")
            sleep(2)
            continue  # Show the todo list again



```




Sources:<br>
w3school:"https://www.w3schools.com/python/python_classes.asp"<br>
youtube tutorial:"https://www.youtube.com/watch?v=vsLBErLWBhA"<br>
MDN:"https://developer.mozilla.org/en-US/docs/Web/HTML"<br>
To-do:"https://pub.aimind.so/creating-a-simple-to-do-list-in-python-c0f52ab15814"<br>


