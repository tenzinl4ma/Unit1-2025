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
