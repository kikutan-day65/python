import re

string = "search inside of this text plz!"

a = re.search("this", string)

# shows a span of the given string
print(a.span())

# shows a start point of the given string
print(a.start())

# shows an end point of the given string
print(a.end())

# shows a start point of the given string
print(a.group())


pattern  =re.compile("software")
string2 = "software: I want to be a software engineer"

b = pattern.search(string2)
c = pattern.findall(string2)
d = pattern.fullmatch(string2)
e = pattern.match(string2)
print(b.group())
print(c)
print(d) # None cuz "software" is not exactly same sentence as string2
print(e)