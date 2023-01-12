# 2D list (mutidimensional list) = a list of list

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

# conteanate each list
menus = [drinks, dinner, dessert]

# show elements in 2d list
print(menus)

# output shold be elements in drinks
print(menus[0])

# output should be hotdog
print(menus[1][2])

print()

# show all of the elements in food 2d list by using nested for loops
for menu in menus:
    for food in menu:
        print(food)
    print()