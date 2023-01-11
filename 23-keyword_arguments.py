# keyword arguments = arguments preceeded by an identifier when we pass them to a function
#                     The order of  the arguments doesn't matter, unlike positional arguments
#                     Python knows the name of the arguments that our function receives



def hello(first, middle, last):
    print("Hello, " + first + " " + middle + " " + last)

# arguments can be written in unordered ny using keyword argument
hello(last="Mori", first="Haruto", middle="Praha")