

my_set = {char for char in "hello"}
#print(my_set)

my_set2 = {num for num in range(0,100)}
# print(my_set2)

my_set3 = {num * 2 for num in range(0, 100)}
# print(my_set3)

my_set4 = {num**2 for num in range(0, 100) if num % 2 == 0}
print(my_set4)

simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
my_dict = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict2 = {num:num**2 for num in [5,6,7]}
print(my_dict2)