# a function that changes the vowels in a string to numbers such as a=4,e=3,i=1,o=0 and space by _



<img width="914" alt="Screenshot 2024-10-01 at 9 46 46" src="https://github.com/user-attachments/assets/104d435d-2d9d-4013-85aa-9e04c2e70fee">

# Code
```.py
def transform_message(msg):
    replacements = {'a': '4', 'e': '3', 'i': '1', 'o': '0', ' ': '_'}
    return ''.join(replacements.get(c.lower(), c) for c in msg)

# Test cases
print(transform_message("Hello World"))  # Expected: "H3ll0_W0rld"
print(transform_message("Why did I choose CS?"))  # Expected: "Why_d1d_1_ch00s3_CS?"
print(transform_message("Remember the Figure Caption"))  # Expected: "R3m3mb3r_th3_F1gur3_C4pt10n"

```


# Evidence
<img width="415" alt="Screenshot 2024-10-03 at 0 51 41" src="https://github.com/user-attachments/assets/cd1fedc3-8439-4574-af6a-c3eba5efb363">
