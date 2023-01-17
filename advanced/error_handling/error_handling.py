# Error Handling

"""
SyntaxError cuz the function doesn't have colon(:)

def foo()
    pass

foo()
"""

"""
NameError cuz name is undefined

def foo():
    1 + name

foo()
"""

"""
IndexError cuz li[5] is out of range

def foo():
    list = [1,2,3]
    li[5]

foo()
"""

"""
KeyError cuz the key 'c' doesn't exist

def foo():
    dict = {'a': 1, 'b': 2}
    dict['c']

foo()
"""

"""
ZeroDivisionError cuz nominator cannot be divided by 0

def foo():
    return 5 / 0

foo()
"""

# How do we avoid these errors above??