import time
import sys

def overwrite_text():
    # Print "Hello"
    sys.stdout.write("Hello")
    sys.stdout.flush()

    # Wait for 2 seconds
    time.sleep(2)

    # Move the cursor back to the beginning of the line and overwrite "Hello" with spaces
    sys.stdout.write("\r" + " " * len("Hello"))
    sys.stdout.flush()

    # Move the cursor back to the beginning of the line again and print "World"
    sys.stdout.write("\rWorld")
    sys.stdout.flush()

# Call the function
overwrite_text()
