# list, set, dictionary

my_list = []

for char in "hello":
    my_list.append(char)
print(my_list)

# it returns the same output above but written only in oneline
your_list = [char for char in "hello"]
print(your_list)


my_list2 = [num for num in range(0,100)]
print(my_list2)


my_list3 = [num * 2 for num in range(0, 100)]
print(my_list3)


my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)