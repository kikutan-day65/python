# this is pure function cuz it doesn't affect anything outside
# if it has return print(newl_list), it isn't pure functio anymore!
# if new_list = [] is outside of function, it gets changeable by any programmers
# --> means error occurs easily
def multiply_by2(list):
    new_list = []

    for item in list:
        new_list.append(item * 2)
    
    return new_list

print(multiply_by2([1,2,3]))

