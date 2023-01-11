# index operator [] = gives access to a squence's element (str, list, tuples)

name = "haruto MORI"


# .islower()/isupper() = check if the index is in lowercase/uppercase
if (name[0].islower()):
    name = name.capitalize()
print(name)


# create a substring
firstName = name[:6]
print(firstName)

lastName = name[-4:].lower()
print(lastName)

lastCharacter = name[-1]
print(lastCharacter)