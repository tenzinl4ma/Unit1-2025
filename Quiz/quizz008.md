# Below code give us the name of the all rooms in 10 floor building

# Flowchart
 
![Screenshot 2024-09-11 at 13 33 04](https://github.com/user-attachments/assets/3dc2514d-1d05-4e6f-8b64-47326b105005)


# Question
 
![Screenshot 2024-09-11 at 13 26 28](https://github.com/user-attachments/assets/9835f316-4417-4505-93ad-ec9ef00883d8)


# Code

```.py
def allroomname():
    roomnumber = 1 
    for floor in range(1, 11): 
        for room in range(1, 11): 
            print(f"{roomnumber}-Room {floor}F{room:02d}")
            roomnumber += 1 

allroomname()

```

# Proof
<img width="1129" alt="Screenshot 2024-09-11 at 13 25 25" src="https://github.com/user-attachments/assets/86137040-1caa-4e23-9341-cea6f457755f">
