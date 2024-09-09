
def validate_int(msg:str)->int:
    unsafe_data= input(msg)
    safe = True
    for letter in unsafe_data:
        if letter not in '0123456789-':
            output = False
        if safe:
            output= int(unsafe_data)
        else:
            output = None
        return output
# calling the function
n= validate_int(msg="enter")
if n is not None:
    exit('The number is not an vlaid inter')
else:
    output = None



# boolean
def validate_bool(msg:str)->bool:
    unsafe_data= input('Enter true or false')
    if unsafe_data in ['false','False', '0']:
        output= False
    elif unsafe_data in ['True', 'true', '1']:
        output= True
    else:
        output = None
    return output

# banner
def banner_maker(msg:str,cols:int,rows:int,symbol='#')->str:
    row_end_start= symbol*cols
    row_middle= symbol + ' '*(cols-2)+symbol
    row_msg = symbol+ ' '*(cols//2-len(msg)//2-1)+msg+ ' '*(cols-len(msg)//2)+symbol
    output= row_end_start + "\n"
    for r in range(rows-3):
        output+=row_middle+ '\n'
    output+=row_middle+ '\n'
    for r in range(rows-3):
        output+=row_middle+ '\n'
    output+=row_middle+ '\n'

