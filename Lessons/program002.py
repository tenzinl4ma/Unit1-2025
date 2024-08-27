#program to count how many Small case and Capital case in the Input words

sentence = input("Enter a sentence: ")

lower_count = 0
upper_count = 0
digit_count = 0
special_count = 0
for letter in sentence:
    if letter.islower():
        lower_count += 1
    elif letter.isupper():
        upper_count += 1
    elif letter.isdigit():
        digit_count += 1
    elif letter!=(lower_count+upper_count+digit_count):
        special_count += 1
total = lower_count + upper_count + digit_count + special_count
print(f"Total Characters: {total}. Lowercase letters: {lower_count}. Uppercase letters: {upper_count}. Digits: {digit_count}  special letters: {special_count}" )
