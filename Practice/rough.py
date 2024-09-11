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
