"""
4 pillars of OOP:
    1. Abstraction
    2. Encapsulation
    3. Inheritance
    4. Polymorphism
"""

# everything is built by a class keyword
# output should be <class '~~~~~'>
print(type(None))
print(type(True))
print(type([])) # list
print(type(())) # tuple
print(type({})) # dict
print(type(5))

# objects have methods and atributes that you can access with DOT method


class BigObject: # Class
    # code
    pass

obj1 = BigObject() # instanciate
obj2 = BigObject() # instanciate
obj3 = BigObject() # instanciate

print(type(obj1))