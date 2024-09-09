# advance python program to create todo list
from time import sleep


import os

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
    if password=="tenzin123":
        print('''These are the list of the password:
    d
    d
    d
    d
    d
    d
    d
    d
    d
    ''')
    else:
        print(" Your password is wrong")
        todo_list()


def todo_list():
    print("""

    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██╗    ████████╗ ██████╗     ████████╗██╗  ██╗███████╗
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝██║    ╚══██╔══╝██╔═══██╗    ╚══██╔══╝██║  ██║██╔════╝
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  ██║       ██║   ██║   ██║       ██║   ███████║█████╗  
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝       ██║   ██║   ██║       ██║   ██╔══██║██╔══╝  
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗██╗       ██║   ╚██████╔╝       ██║   ██║  ██║███████╗
     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝       ╚═╝    ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝




        """, end='', flush=True)
    sleep(2)


    os.system('cls' if os.name == 'nt' else 'clear')

        # Print the second large ASCII message
    print("""   
    ████████╗ ██████╗     ██████╗  ██████╗     ██╗     ██╗███████╗████████╗██╗
    ╚══██╔══╝██╔═══██╗    ██╔══██╗██╔═══██╗    ██║     ██║██╔════╝╚══██╔══╝██║
       ██║   ██║   ██║    ██║  ██║██║   ██║    ██║     ██║███████╗   ██║   ██║
       ██║   ██║   ██║    ██║  ██║██║   ██║    ██║     ██║╚════██║   ██║   ╚═╝
       ██║   ╚██████╔╝    ██████╔╝╚██████╔╝    ███████╗██║███████║   ██║   ██╗
       ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝     ╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝

    """, end='', flush=True)
    sleep(2)
    tasks = []
    print("\r   \033[1m           This is a simple to do list \U0001f600", end='', flush=True)
    while True:
        action = input("Choose an action: [add/view/remove/quit]: ").strip().lower()
        if action=='admin':
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
