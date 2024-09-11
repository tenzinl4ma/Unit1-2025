# advance python program to create todo list
import os

from time import sleep
from validation import color
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
def sleepmac():
    print("Trial limit exceeded. Putting the laptop to sleep...")
    os.system("pmset sleepnow")

def passwordmanagers():
    print("Opening the secret Cretentials.")
    sleep(2)
    print("Opening the secret Cretentials..")
    sleep(2)
    print("Opening the secret Cretentials...")
    sleep(2)
    print("Opening the secret Cretentials....")
    sleep(2)
    password=input(" You need to input the password")
    max=3
    for i in range(max):
        i+=1
    if password == "tenzin123":
            print(color.bg.red+'''
The secret recipe of the coca-cola
# 1 teaspoon of the salt and sugar
# 2 mug of the honey 
# 3 water and sand
        '''+color.reset)
    else:
            print(" Your password is wrong")
    todo_list()



def todo_list():
    tasks = []
    print("\r   \033[1m           This is a simple to do list \U0001f600", end='', flush=True)
    while True:
        action = input("Choose an action: [add/view/remove/quit]: ").strip().lower()
        if action=='sudouser':
            passwordmanagers()
        if action == 'add':
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added.")
        elif action == 'view':
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif action == 'remove':
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_num = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_num < len(tasks):
                removed_task = tasks.pop(task_num)
                print(f"Removed task: {removed_task}")
            else:
                    print("Invalid task number.")
        elif action == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid action.")
todo_list()
