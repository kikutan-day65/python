
# reading a file
try:
    with open('C:\\Users\\bayst\\coding\\python\\files\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("that file is not found")


# add new sentences to the file
text = "Haruto Mori\nFrom Japan\nI'm a big fan of the Baystars\n"

with open('C:\\Users\\bayst\\coding\\python\\files\\test2.txt', 'w') as file2:
    file2.write(text)


# append new sentences to the file
append = "!!!I'm studying pyhton in the national technical library in prague!!!"

with open('C:\\Users\\bayst\\coding\\python\\files\\test2.txt', 'a') as file2:
    file2.write(append)