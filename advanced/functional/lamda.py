# lamda expressions

from functools import reduce

"""
the lamda function syntax:

    lambda param: action(param), object
"""

my_list = [1,2,3]
your_list = [4,5,6]

"""
These function are no longer needed because of using lamda

def multiply_by2 (item):
    return item * 2


def odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

"""

# lamda fucntion for map()
print(list(map(lambda item: item * 2, my_list)))

# lamda fucntion for filter()
print(list(filter(lambda item: item % 2 != 0, my_list)))

# lamda fucntion for reduce()
print(reduce(lambda acc, item: acc + item, my_list))