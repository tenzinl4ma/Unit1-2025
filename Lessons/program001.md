# Check if weather the given number is prime or even

```.py
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Exclude even numbers greater than 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Validation of user input
num = input("Enter a number: ")

if not num.isdigit():
    print("Invalid Input")
    exit()

num = int(num)  # We can safely convert the input to an integer now

# Print all prime numbers up to the input number
print(f"Prime numbers up to {num}:")
for x in range(2, num + 1):  # Start from 2, the smallest prime number
    if is_prime(x):
        print(x)
```
