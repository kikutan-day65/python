some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

# find duplicates
duplicates = set([x for x in some_list if some_list.count(x) > 1])
list(duplicates)

print(duplicates)

# set doesn't allow duplicates