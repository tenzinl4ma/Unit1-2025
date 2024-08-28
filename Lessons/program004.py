print("   WELCOME TO KIDSMATH")
#show multiplicaton table
#show factors of a number
#show even numbers
def multiplication_table():
    #multiplication table
    print("You chose 1st option")
    a = int(input("Enter a number: "))
    for i in range(1, a + 1):
        print(i * a)
def factorial_num():
    num = int(input("Enter a number: "))
    print("You chose 2nd option")
    for i in range(1, num + 1):
        print(f"factorial of given num is {i}.")

def even_num():
    print("You chose 3rd option")
    c = int(input("Enter a number: "))
    if c % 2 == 0:
        print(f"{c} is an even number")
    else:
        print(f"{c} is not an even number")
ask=int(input("choose 1,2 or 3 for multiplication table, factors,even \n>>>>"))
def asker():
        if ask==1:
            multiplication_table()
        elif ask==2:
            factorial_num()
        elif ask==3:
            even_num()
        elif ask >3:
            print("Num High")
        elif ask <0:
            print("Numb Low")
        else:
            print("invalid input")
asker()
que=input("Do you want to continue? Pres Y for Yes and ")
for y in que:
    asker()
