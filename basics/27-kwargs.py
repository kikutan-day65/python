# **kwawrgs = parameter that will pack all arguments into a DICTIONARY
#             useful so that a function can accept a varying amount of keyword arguments

"""
def hello(first, last):
    print("Hello," + first + " " + last)

hello(first="Haruto", middle="Praha", last="Mori")

this gives a typeError
"""

def hello(**kwargs):
    print("Hello," + kwargs['first'] + " " + kwargs['last'])

    print("Hello,", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Ing.", first="Haruto", middle="Praha", last="Mori")