#dictionary method
mapping = {"A": "T", "T": "A", "G": "C", "C": "G", "ASD":"DSA"}

# Get user input
user = input("Enter a character (A, T, G, C, or ASD): ").upper()
print("You input",user)
# Get the corresponding character from the dictionary
output = mapping.get(user, "Invalid input")
# Print the result
print(f"and it's output is {output}")
