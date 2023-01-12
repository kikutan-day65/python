# tuples = collecton which is ordered and unchangeable
#          used to group together related data

student = ("Haruto", 25, "male")

print(type(student))

# how many "Haruto" is in the student tuple?
print(student.count("Haruto"))

# index() = returns the index of the element
print(student.index("male"))

# show all of the element in the studetn tuple in oneline
for x in student:
    print(x, end=" ")
print()


if "Haruto" in student:
    print("Haruto is a student!")
else:
    print("He's not in the student tuple.")