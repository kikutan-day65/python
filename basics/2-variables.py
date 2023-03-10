# variable = a contaianer for a value. Behaves as the value that it contains

# strings = a series of characters
firstName = "Haruto"
lastName = "Mori"

# print the datatype of the variable
print(type(firstName))
print(type(lastName))

print("Hello, " + firstName + " " + lastName + "\n")


# integer datatype
age = 24

print(type(age))

age = age + 1
print("You're " + str(age) + " years old.\n")


# float = floating point number (a decimal number)
height = 171.5

print(type(height))
print("Your height is " + str(height) + "cm\n")


# boolean = True or False
human = True
animal = False

print(type(human))
print(type(animal))

print("You're human: " + str(human))
print("You're an animal: " + str(animal) + "\n")


# multiple assignment = allows us to assign multiple variables at the same time in one line of code
name, age, attractive = "Yazan", 19, True

print(name)
print(age)
print(attractive)