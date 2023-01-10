# input() = allows user to input and take it as a string. you have to surround datatype such as int(), float() if you want a specific datatype
name = input("What is your name?: ")

# it returns error if user typed diffrent datatype
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))


print("Hello, " + name)
print("You're " + str(age) + " years old")
print("You're " + str(height) + " cm")