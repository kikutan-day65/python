# slicing = create a substring by extractiong elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Haruto Mori"

firstName = name[:6] # name[0:6] works as the same!
lastName = name[7:] # name[7:11] works as the same!
funkyName = name[::2] # name[0:11:2] works as the same!

reversedName = name[::-1]

print(firstName)
print(lastName)
print(funkyName)
print(reversedName)