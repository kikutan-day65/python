# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

"""
def add(num1, num2):
    sum = num1 + num2
    return sum

print(add(1,2,3))

This gives a typeError
"""

# *args argument takes all the input as a tuples, *args can be changed any name
def add(*args):
    # shows a tuple
    print(args)

    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))