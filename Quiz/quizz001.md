# The program to to produce first and last word and sum middle one
## Question slide image
<img width="999" alt="Screenshot 2024-08-29 at 14 15 55" src="https://github.com/user-attachments/assets/0fb0474d-5657-4272-a016-c2625adb4bee">

# Flowchart
![Screenshot 2024-08-31 at 19 17 02](https://github.com/user-attachments/assets/b2fd8326-3557-41ff-a594-250c24b658fb)


# Code
```.py
# Array of five words given in class
words = ["internationalization", "localization", "Hello world !", "98 99 100 101 1062", "(codin) + (game) = (codingame)"]

# shorten the words and join them together
shorten = [
    ' '.join([w[0] + str(len(w) - 2) + w[-1] if len(w) > 2 else w for w in word.split()])
    for word in words
]

# Print each shorten word
for shorten_words in shorten:
    print(shorten_words)
```

# Proof
<img align="center" width= 800 height="300" src="https://github.com/user-attachments/assets/eac83fee-2b61-42b2-baca-1448896f79b1">
