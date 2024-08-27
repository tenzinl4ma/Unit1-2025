

##Python program to anagram check. Check if there is common letter between two words and ask user to continue game or quit
print("Python program to check anagram")
def x():
    word= input("Enter a first word: ")
    word2= input("Ener a second word")
    s=set(word)
    r=set(word2)
    if s & r:
        print(f"The anagram of word{word} is in {word2}")
    else:
        print(" It fail the anagram test.")
    ask= input("Do you want to continue (yes or no): ")
    if ask=="yes" or ask=="y":
        x()
    else:
        exit()
x()
