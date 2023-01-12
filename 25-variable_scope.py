# scope = The regiion that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

import math

# globalName can be accesses from anywhere
globalName = "Yazan"

def display():
    # localName cannot be accessed from the outside of function
    localName = "Haruto"
    print(localName)
    print(globalName)

display()

#global scope 
PI = 3.14

def area(dia):
    return pow(dia, 2) * PI

def circumference(dia):
    return (dia * 2) * PI

diameter = float(input("Enter the length of diameter: "))

area = area(diameter)
circum = circumference(diameter)

print(area)
print(circum)