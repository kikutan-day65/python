# map, filter, zip, and reduce

"""
def multiply_by2(list):
    new_list = []
    for item in list:
        new_list.append(item * 2)
    
    return new_list

print(multiply_by2, [1,2,3])

Insted, we can write ...
"""

my_list = [1,2,3]

# map()
def multiply_by2 (item):
    return item * 2

print(list(map(multiply_by2, my_list))) # it returns [2,4,6] with map()
print(my_list) # however, my_list is not changed!
