"""
absolute path = the complete details needed to locate a file or folder,
                starting from the root element and ending with the other subdirectories.
                "C:\Users\bayst\coding\python\file_IO\script.py"

relative path = the path related to the present working directly(pwd). 
                It starts at your current directory and never starts with a / .
                "./app/happy.txt ---> ./ means from the current folder"

"""


my_file = open("test.txt")

# shows the file content
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0)

print()

# shows the file contents by line
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.seek(0)

print()

# shows the file contents by line as a list
print(my_file.readlines())

# close the file
my_file.close()