# Program To Translate DNA Chain 
### Flowchart
![Flowchart3](../../../../../../../../var/folders/vz/frkd5v5x24vf1fpv9h7qrtvc0000gp/T/TemporaryItems/NSIRD_screencaptureui_OG9Rsk/Screenshot%202024-08-28%20at%2023.19.41.png)
## Question from slide:
![Question_Screenshot](../../../../../../../../var/folders/vz/frkd5v5x24vf1fpv9h7qrtvc0000gp/T/TemporaryItems/NSIRD_screencaptureui_GTQXlH/Screenshot%202024-08-28%20at%2023.10.54.png)
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
![Quiz3proof](../../../../../../../../var/folders/vz/frkd5v5x24vf1fpv9h7qrtvc0000gp/T/TemporaryItems/NSIRD_screencaptureui_g4Id1N/Screenshot%202024-08-29%20at%200.20.19.png)
