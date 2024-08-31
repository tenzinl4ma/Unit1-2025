# 
quizzes are checked **every 8** quizzes
## Flowchart



## Code 
```.py
# this code take input from user and compare
num= int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num == 20 or num2==20 or num + num2==20:
    print(f"{num}:{num2}: True")
else:
    print(f"{num}:{num2}: False")

#this one all the data are given in array
# quiz given number in array
number_pairs = ["30:10", "30:5", "30:-10", "200:-180"]
# Function to check each pair
def check_pairs(pairs):
    results = []  # Create an empty list to store the results
    for pair in pairs:
        num1, num2 = pair.split(":")  # Split the pair into two numbers
        num1 = int(num1)  # Convert the first number to an integer
        num2 = int(num2)  # Convert the second number to an integer

        # Check if either number is 20 or if their sum is 20
        if num1 == 20 or num2 == 20 or num1 + num2 == 20:
            results.append(True)  # Add True to results if the condition is met
        else:
            results.append(False)  # Add False if the condition is not met

    return results  # Return the list of results


# Apply the function to the array of number pairs
results = check_pairs(number_pairs)

# Print the results for each pair
for i in range(len(number_pairs)):
    print(number_pairs[i] + ": " + str(results[i]))


# HL
a = [10, 30, 10, 26]
b = [20, 15, 5,-6]

# Check if 30 is in list a or if 20 is in list b
if 20 in a or 20 in b:
    print(f"{a}:{b}: True")
else:
    print("False")


```
