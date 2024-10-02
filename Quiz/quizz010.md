# This program produces the powers of ten from pico (10-12), to tera (1015) for a number provided as an input.












# Code 
```.py

def powersTen(value):
    units = [
        (10 ** 12, 'Tera'),  
        (10 ** 9, 'Giga'),
        (10 ** 6, 'Mega'),  
        (10 ** 3, 'kilo'),  
        (1, 'unit'),  
        (10 ** -3, 'milli'),  
        (10 ** -6, 'micro'),  
        (10 ** -9, 'nano'),  # 0.000000001
        (10 ** -12, 'pico')  # 0.000000000001
    ]

    for x in units:
        for j in x:
            print(f"{value * x:.12f} {j}")
powersTen(1)

```




