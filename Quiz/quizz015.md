# Program that produces the average word length of the input list

<img width="965" alt="Screenshot 2024-10-01 at 9 44 50" src="https://github.com/user-attachments/assets/fc01baaf-d05d-4c31-b5f6-11d9375aebcb">


# Code
```.py

def averageLength(words):
    total_chars = sum(len(word.replace(" ", "")) for word in words)
    total_words = len(words)
    return total_chars / total_words

# Test cases
print(averageLength(["hello", "main"]))  # Expected: 4.5
print(averageLength(["Peru", "France", "Nepal"]))  # Expected: 5.0
print(averageLength(["Computer Science", "Art"]))  # Expected: 9.5
print(averageLength(["one", "two"]))  # Expected: 3.0

```

# Evidence
<img width="443" alt="Screenshot 2024-10-03 at 0 45 33" src="https://github.com/user-attachments/assets/9d4f11c9-fde5-4c59-9a59-a61d4595e53c">
