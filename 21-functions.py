# function = a block of code which is executed only when it is called

def hello(firstName, lastName):
    print("Hello! " + firstName + " " + lastName)
    print("Have a nice day.")


first = input("Enter your firstname: ")
last = input("Enter your lastname: ")

if first.isalpha() and last.isalpha():
    hello(first, last)
else:
    print("invalid name")


