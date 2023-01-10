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


# .capitalize() = capitalize the FIRST letter of the string
cap = name.capitalize()
print(cap + "\n")


# .upper(), .lower() = it convert a string to uppercase/lowercase
uppercase = name.upper()
lowercase = name.lower()
print(uppercase)
print(lowercase + "\n")


# .isdigit() = it returns boolean(True/False) if a string is digit
digit = name.isdigit()

if digit:
    print("Yes, it is digit\n")
else:
    print("No, it is not digit\n")


# .isalpha = it returns boolean(True/False) if a string is alphabet without blanck space
string = "Konnichiwa"
alpha = string.isalpha()

if alpha:
    print("Yes, it is alphabet\n")
else:
    print("No, it is not alphabet\n")