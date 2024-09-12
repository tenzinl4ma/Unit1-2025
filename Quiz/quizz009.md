# This is cipher code which encrypt the message by shifting its positon

# Flowchart


# Paperwork



# Code

```.py
def shifter():
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    inpput = input("Enter the string: ").lower()
    store = []
    if "secret" in inpput:
        shift = -10
    else:
        shift = 13
    for char in inpput:
        if char in alphabets:
            indexx = (alphabets.index(char) + shift) % 26
            store.append(alphabets[indexx])
        else:
            store.append(char)
    print("Shifted string:", ''.join(store))
shifter()
```

# Proof

<img width="611" alt="Screenshot 2024-09-11 at 21 31 03" src="https://github.com/user-attachments/assets/ee34435b-77ca-4265-9423-9bfe95d2a649">
