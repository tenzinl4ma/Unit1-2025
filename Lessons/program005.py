characters='1abcdefghijklmnopqrstuvwxyz'
word=input('Enter a word: ').lower()
total=[]
for letter in word:
    if letter in characters:
        position= characters.index(letter)
        total.append(position)
print(sum(total))