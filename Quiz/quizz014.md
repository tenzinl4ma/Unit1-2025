###  There are N closed doors in a school and N students present. The first student opens each door. The second student flips (open⇆close) every second door. The third student flips every third door, and so on. 

# Question/Prompt
<img width="1195" alt="Screenshot 2024-10-01 at 9 12 50" src="https://github.com/user-attachments/assets/0bb4d89f-769b-4b9b-85d4-c2ef2b1bed8a">
# Flowchart

![Screenshot 2024-10-03 at 0 38 23](https://github.com/user-attachments/assets/d08b6f5b-df83-4136-9513-4491015cb6fd)


# Code 
```.py

def open_doors(num_students):
    return int(num_students ** 0.5)
num_students_list = [10, 100, 200, 5678]
for num_students in num_students_list:
    open_doors_count = open_doors(num_students)
    print(f"Number of students: {num_students}, Open doors: {open_doors_count}")
```

# Evidence
<img width="402" alt="Screenshot 2024-10-02 at 23 06 31" src="https://github.com/user-attachments/assets/88aaa9f6-41a6-4215-8cb6-1e34e388d858">
