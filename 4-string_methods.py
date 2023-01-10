name = "Haruto Mori"

# len() = how long the string is
length = len(name)
print("string length is: " + str(length) + "\n")

# .find() = find the designasted letter in the string. it returns the inde of it.
place = name.find("H")
print("\"H\" is at idx " + str(place) + "\n")

# it returns the first one if a string contains the same letter
place = name.find("o")
print("\"o\" is at idx " + str(place) + "\n")

place = name.find("Mori")
print("\"Mori\" is started at idx " + str(place) + "\n")
