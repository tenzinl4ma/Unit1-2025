# Program To Translate DNA Chain 
### Flowchart

![Flowchart](https://github.com/user-attachments/assets/369df598-6b35-4642-9395-5fcc95cdda36)

## Question from slide:
<img width="1214" alt="Screenshot 2024-08-29 at 0 33 12" src="https://github.com/user-attachments/assets/9a209d9c-e7cb-459c-ae1f-22ff0b1350c2">

## Code
```.py
mapping = {"A": "T", "T": "A", "G": "C", "C": "G", "ASD":"DSA"}

# Get user input
user = input("Enter a character (A, T, G, C, or ASD): ").upper()
print("You input",user)
# Get the corresponding character from the dictionary
output = mapping.get(user, "Invalid input")
# Print the result
print(f"and it's output is {output}")
```
# Proof 

![Screenshot 2024-08-29 at 0 31 46](https://github.com/user-attachments/assets/07ab2abc-a8c4-465a-83c1-68e31cfe0a19)