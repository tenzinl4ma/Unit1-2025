# an program to check wether the word provide is palindrome or not

word= input("please enter the word\n>>>")
rev= word[::-1]
print(f"you input the word {word} and the reversed word is {rev}")
if word==rev:
    print('So, its a palindrome')
else:
    print('So, its not a palindrome')