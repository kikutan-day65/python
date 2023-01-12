# list = used to store multiole items in a single variable

food = ["pasta", "tomato", "ham", "onion"]

print(type(food))
print(food)

# show all of the elements in food list
for i in food:
    print(i)
print()


# append element to food list
food.append("ice cream")
for i in food:
    print(i)
print()


# remove element in food list
food.remove("tomato")
for i in food:
    print(i)
print()

food.remove(food[0])
for i in food:
    print(i)
print()


food = ["pasta", "tomato", "ham", "onion"]

# pop() = remove the last elemnt in the list 
food.pop()
for i in food:
    print(i)
print()


# insert(A, B) = insert the element B at the position A
food.insert(1, "beef")
for i in food:
    print(i)
print()


# sort() = sort element alphabetically in the list
food.sort()
for i in food:
    print(i)
print()


# clear() = remove all of the elements in the list = rerturns nothing
food.clear()
for i in food:
    print(i)
print()