# A program to print the Calendar 
### first create the list of the days and then dates
### import self made color library and then python datetime libray

# Question
<img width="1149" alt="Screenshot 2024-10-01 at 9 05 54" src="https://github.com/user-attachments/assets/0e5f4268-f82e-4f2f-8327-b0035e8d27c1">

# Flowchart
<img width="263" alt="Screenshot 2024-09-18 at 17 59 16" src="https://github.com/user-attachments/assets/498a84ef-9c3a-42f2-a14d-12788c5e25e2">


# Code
```.python
from validation import color
from datetime import datetime
print(color.bg.red,"Current Year:   ",datetime.now().strftime("%Y %H:%M"),color.reset_all)

days = [color.bg.yellow,"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",color.reset_all]
april_days = [
[color.bg.blue," 1", "  2", "  3", "  4", "  5", "  6", "  7",color.reset_all],
    [color.bg.blue," 8", "  9", " 10", " 11", " 12", " 13", " 14",color.reset_all],
    [color.bg.blue,"15", " 16", " 17", " 18", " 19", " 20", " 21",color.reset_all],
    [color.bg.blue,"22", " 23", " 24", " 25", " 26", " 27", " 28",color.reset_all],
    [color.bg.blue,"29", " 30", "    ", "    ", "    ", "    ",color.reset_all]
]

# Print header
print(" ".join(days))

# Print the weeks with the extra space added to each date
for week in april_days:
    print(" ".join(week))
```

# Proof
<img width="1147" alt="Screenshot 2024-09-18 at 17 46 48" src="https://github.com/user-attachments/assets/9aa2da57-3c07-47f5-9851-145a847d452b">

