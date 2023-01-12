# OS module provides the facility to establish the interaction between the user and the operating system.
import os

path = "C:\\Users\\bayst\\coding\\python\\files\\test.txt"

# hceck if the location is exist on your pc
if os.path.exists(path):
    print("that location exists!")

    # check if it is a flie, a folder, or
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a folder")
else:
    print("that location doesn't exist!")