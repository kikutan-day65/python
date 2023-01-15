# map, filter, zip, and reduce

my_list = [1,2,3]
your_list = [10,20,30]
their_list = [5,4,3]

def multiply_by2 (item):
    return item * 2

def odd(item):
    return item % 2 != 0


print(list(zip(my_list, your_list, their_list))) # it returns [(1, 10, 5), (2, 20, 4), (3, 30, 3)] with zip()
print(my_list) # however, my_list is not changed!


my_tuple = (5,6,7)
your_tuple = (50,60,70)

print(list(zip(my_tuple, your_tuple)))
print(my_tuple)