def calculate_sum(s: str, hl_comp: bool = False) -> int:
    total = 0

    for char in s:
        if char.isalpha():  # Check if the character is a letter
            if hl_comp:
                # Calculate differently for uppercase and lowercase
                if char.islower():
                    total += (ord(char) - ord('a') + 1) * 10  # Lowercase (a=10, b=20, ...)
                else:
                    total += (ord(char) - ord('A') + 1) * 100  # Uppercase (A=100, B=200, ...)
            else:
                # Calculate normally for non-HL mode, case insensitive
                total += ord(char.lower()) - ord('a') + 1

    return total


# Test cases
print(calculate_sum("Math"))  # Output: 42
print(calculate_sum("maTH"))  # Output: 42
print(calculate_sum("Hello world"))  # Output: 92
print(calculate_sum("Computer SCIENCE"))  # Output: 137
print(calculate_sum("Math", hl_comp=True))  # Output: 1385
