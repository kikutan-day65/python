# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}


utensils.add("napkin")

# print out the element in the utensils set but order is different in each execution
for x in utensils:
    print(x)
print()


utensils.remove("fork")

for x in utensils:
    print(x)
print()


dishes = {"bowl", "plate", "cup"}

# update() = update the element of a set = integrate two sets
utensils.update(dishes)

for x in utensils:
    print(x)
print()


# union() = integrates sets by bahaving a union operation. python has set operation method such as union(), difference()
dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)
print()