# 2D list (mutidimensional list) = a list of list

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

# conteanate each list
food = [drinks, dinner, dessert]

# show elements in 2d list
print(food)

# output shold be elements in drinks
print(food[0])

# output should be hotdog
print(food[1][2])

print()

# show all of the elements in food 2d list by using nested for loops
for menu in food:
    for item in menu:
        print(item)
    print()