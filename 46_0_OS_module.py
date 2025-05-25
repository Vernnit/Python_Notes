# The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.


import os

# Open the file in read-only mode
f = os.open("Requirements.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

# Close the file
os.close(f)


import os

# Open the file in write-only mode
f = os.open("requirements.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")
print(f)

# Close the file
# os.close(f)