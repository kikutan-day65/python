# wirte a code to get numbers squared with lamda expression
my_list = [5,4,3]

result = list(map(lambda item: item ** 2, my_list))
print(result)


# sort the list based on the 2nd value of the tuple with lamda expression
a = [(4,3), (0,2), (9,9), (10, -1)]

a.sort(key=lambda tpl: tpl[1])
print(a)