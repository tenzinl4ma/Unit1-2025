# This is program scramble the password from the provided list


### It generate random password to minimize the risk of the bruteforce and guess


# Flow-Chart

<img width="458" alt="Screenshot 2024-09-08 at 22 27 23" src="https://github.com/user-attachments/assets/7132c7cc-2491-457c-8b3d-05a9921dbdc6">

### question flowchart image

# Code

```.py
def password_scrambler(K):
    N = len(K)  
    R = [] 
    for x in range(N):
        for y in range(N):
            R.append(K[x] + K[y])  
    return R

K = ['pass', '123', 'word', '1']
result = password_scrambler(K)
print(result)

```
# Proof  

<img width="1626" alt="Screenshot 2024-09-08 at 22 40 41" src="https://github.com/user-attachments/assets/7907389d-b475-4685-944b-9f6d9a491110">











