## User input conditionalizer
### Given two numbers, A and B, Output TRUE if one of them is 20 or sum is 20
#### zip()function: use to combine multiple iterals in parallel
## Question Slide
<img width="1189" alt="Quiz_question2" src="https://github.com/user-attachments/assets/9a53fa2f-d7fc-47e7-a3cb-a263fbcbab0a">

# Flowchart
<img width="555" alt="Screenshot 2024-08-29 at 1 33 19" src="https://github.com/user-attachments/assets/501f10b6-b430-4c45-a0c6-f19e5b971870">

# Code
```py.
print(" two number if one is 20 or their sum is 20 it will print True else False")
num1_list = [30, 30, 30, 200]
num2_list = [10, 5, -10, -180]

for num1, num2 in zip(num1_list, num2_list):
    if num1 == 20 or num2 == 20:
        result = True
    elif num1 + num2 == 20:
        result = True
    else:
        result = False
    print(f"num1: {num1}, num2: {num2} => result: {result}")
```



# Proof
![Quize2_proof](https://github.com/user-attachments/assets/d485c71e-e97f-4f2b-8d2d-1998615875de)
