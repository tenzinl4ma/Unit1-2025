#program to print the even number from array of data and you can add the num in array
#Know reduce function
#Used append funtion
from functools import reduce
numbers = []
n=int(input("Enter how many numbers you want to enter in place"))
for i in range(n):

    numbers.append(int(input("Enter a numbers that you want it to be sum of in total")))
    print(numbers)
product = reduce(lambda x,y: x+y, numbers)
print(f" so the total sum of all the number:{numbers} is: {product}")

print("\U0001F600")
print("\U0001F600")
print("\U0001F600")
