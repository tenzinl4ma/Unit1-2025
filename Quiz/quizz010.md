# This program produces the powers of ten from pico (10-12), to tera (1015) for a number provided as an input.


# Question
![Screenshot 2024-10-02 at 17 41 22](https://github.com/user-attachments/assets/a2335cd7-8796-4fe2-b2c1-02510404956c)


# Flowchart
![Screenshot 2024-10-02 at 18 10 12](https://github.com/user-attachments/assets/c7dabe1b-1b05-4974-bc4b-c84807081546)



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
        (10 ** -9, 'nano'),
        (10 ** -12, 'pico')
    ]

    for x, j in units:
        print(f"{value * x:.12f} {j}")
powersTen(1)



```


# Evidence

<img width="423" alt="Screenshot 2024-10-02 at 13 35 36" src="https://github.com/user-attachments/assets/328d5e35-d1d7-4f26-8ec0-4fd17dbdbaf2">

