import os
import random


def sleep_laptop():
    print("Trial limit exceeded. Putting the laptop to sleep...")
    os.system("pmset sleepnow")  # Puts Mac into sleep mode


def guess_number_game():
    number_to_guess = random.randint(1, 10)
    trials = 0
    max_trials = 3

    while trials < max_trials:
        guess = int(input("Guess the number between 1 and 10: "))
        trials += 1

        if guess == number_to_guess:
            print("Congratulations! You've guessed the number.")
            break
        else:
            print("Wrong guess. Try again.")

    if trials == max_trials:
        sleep_laptop()


guess_number_game()

trials = 0
max_trials = 3
while trials < max_trials:
    trials += 1
    if trials == max_trials:
        sleepmac()