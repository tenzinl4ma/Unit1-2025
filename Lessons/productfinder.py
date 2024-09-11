#product_finder.py
#r for read only
#W write only
#a appends to existing or new file
from validation import color
with open ('database.csv', 'r') as f:
    data= f.readlines()
with open ('database.csv', 'a') as f:
    f.writelines(['bread, 50 \n', 'banana, 100\n'])
catalog={}
for item in data:
    remove_new_line=item.strip()
    print(item)
    name,price= remove_new_line.split(',')
    catalog[name]=int(price)
terminate= True
while terminate:
    item_unsafe=input(f" {color.bg.yellow}what item are you looking for?{color.reset}")
    item_requested= item_unsafe.lower()
    if item_requested=='x':
        terminate= False
    elif item_requested=='w':
        print('hello')

    # we want to add a new item to the database/catolog
    #ask user for name
    # check that the name is not already in the database
    #

    else:
        print(f" {item_requested}=¥{catalog[item_requested]}{color.reset}")
