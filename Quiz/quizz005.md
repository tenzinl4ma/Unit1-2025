# This program use a new function called ord to get the value of character


# flowchart
![Screenshot 2024-09-11 at 13 47 25](https://github.com/user-attachments/assets/f5eabab4-6ed9-487a-a399-75bab4dc4e14)


# Question
![Screenshot 2024-09-11 at 13 43 40](https://github.com/user-attachments/assets/31450ffb-aeda-496a-8584-e1ad32273d30)

 
# Code

```.py
def sumcharacters(string):
    totalsum = 0

    for char in string:
        if char.isalpha():
            char = char.lower()
            totalsum += ord(char) - ord('a') + 1

    return totalsum


string_input = "Math"
result = sumcharacters(string_input)
print(f"The sum of characters in '{string_input}' is {result}.")


```


# Proof

<img width="637" alt="Screenshot 2024-09-11 at 13 48 24" src="https://github.com/user-attachments/assets/775eacb4-8703-46c9-8edd-e3b875bc372b">




