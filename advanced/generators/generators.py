# iterable
# iterate
# generators

def generator_func(num):
    for i in  range(num):
        yield i * 2

for item in generator_func(1000):
    print(item)

g = generator_func(100)
print(g)

next(g)
next(g)
print(next(g))

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list = make_list(100)
# print(my_list)