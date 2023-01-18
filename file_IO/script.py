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