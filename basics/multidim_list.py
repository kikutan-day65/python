
matrix = [
    [1,2,3],
    [4,5,6,7, 8],
    [9,10,11,12,13,14,15]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()


name_list = []

rows = int(input("How many rows in 2D list?: "))
users = int(input("How many names in the row?: "))

# generate the rows in a given list
for row in range(0, rows):
    name_list.append([])
    # decide a number of names in the row
    for name in range(0, users):
        name = input("Enter names: ")
        name_list[row].append(name)

print(name_list)