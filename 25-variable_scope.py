# scope = The regiion that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created


# globalName can be accesses from anywhere
globalName = "Yazan"

def display():
    # localName cannot be accessed from the outside of function
    localName = "Haruto"
    print(localName)
    print(globalName)

display()