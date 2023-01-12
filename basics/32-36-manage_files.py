
try:
    with open('C:\\Users\\bayst\\coding\\python\\files\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("that file is not found")