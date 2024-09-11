
f = Figlet(font='slant')
print(f.renderText('text to render'))


def triangle():
    tri=180
    angle1= int(input("please enter the angle A"))
    angle2= int(input(" plase enter the angle B"))
    angle3= int(input(" plase enter the angle C"))
    if angle1+angle2+angle3== tri:
        print(True)
    else:
        print(False)
#triangle()
##second one
def rightanlgetri():
    print("Hypotanous of the right anlge triangle calculator")
    side1=int(input("Please enter the base triangle"))
    side2=int(input("Please enter the adjacent triangle"))
    sumsquared=(side1**2)+side2**2
    hypotaneous=sumsquared*0.5
    print(f" Your base is: {side1} and adjacent is: {side2} and calculated hypotanous is :{hypotaneous}")
#rightanlgetri()

##third one
def base2converter():
    base10=25
    allremainder=[]
    while base10>0:
        remainder= base10%2
        allremainder.append(remainder)
        base10=base10//2
    print(allremainder)
    reaminder= allremainder[::-1]
    print(reaminder)
#base2converter()
def lastwordcount():
    word=input("please enter a word:")
    space=word.split()
    print(f" The sentence that you enter is {word} and the len of the last word is {len(space[-1])}")
#lastwordcount()
##print the word till the number
def counterrr():
    n = 6
    alphab = 'abcdefghi'
    result=' '
    for i in range(n):
        result+=alphab[i]
    print(result)
#counterrr()
###
n=3
result=[]
for i in range(1,n+1):
    result.append(i)
print(result)
x=[]
for i in range(n+1,n*2+1):
    x.append(i)
print(x)
y=[]
for i in range(x[-1],x[-1]*2+1):
    y.append(i)
print(y)

'''alpha = 'abcdefghikklmnopqrstuvwxyz'
inputt=int(input("enter the number"))
result=''
for i in range(inputt):
    result+=alpha[i]
print(result)

n=10
p=3
result=[]
for x in range(p):
    for i in range(1,p+1):
        result.append(i)
if len(result)==9:
    result.append(1)
print(result)
from Practice.code001 import result


alpha = 'abCdefghijklmnopqrstuvwxyz'
n = 10
s = 3
result = ''

# Outer loop runs 'n' times
for x in range(n):
    # Add the character from 'alpha' at position 'x % s' to 'result'
    result += alpha[x %s]
print(result)



def create_nested_lists(n):
    # Step 1: Initialize an empty list to hold the final result
    result = []

    # Step 2: Loop n times to create n inner lists
    for _ in range(n):
        # Step 3: For each iteration, create an inner list with the value n
        inner_list = [n]

        # Step 4: Add this inner list to the result list
        result.append(inner_list)

    # Step 5: Return the final result list containing n inner lists
    return result


# Example usage
n = 3
output = create_nested_lists(n)
print(output)  # Output will be [[3], [3], [3]]

n = 4
output = create_nested_lists(n)
print(output)  # Output will be [[4], [4], [4], [4]]
'''

































































