# map, filter, zip, and reduce

my_list = [1,2,3]

def multiply_by2 (item):
    return item * 2

def odd(item):
    return item % 2 != 0

print(list(filter(odd, my_list))) # it returns [1, 3] with filter()
print(my_list) # however, my_list is not changed!