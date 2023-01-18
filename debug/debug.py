# debugging

# linting = allows us to detect as we code some issue with our code
# IDE / editer
# ruead errors

# pdb = python debugger (built-in)
import pdb

def add(num1, num2):
    pdb.set_trace()
    t = 4*5
    return num1 + num2

add(4, "asdf")