# for loop = a statement that will execute its block of code
#            a limited amount of times


# count up
for i in range(10):
    print(i, end=" ")

print("\n")

# count up between 50 and 100
for i in range(50, 100 + 1):
    print(i, end=" ")

print("\n")

# show even numbers between 0 and 100
for i in range(0,100 + 1, 2):
    print(i, end = " ")

print("\n")

# show each letter of a string
word = "pneumonoultramicroscopicsilicovolcanoconiosis"
count = 1

for i in word:
    if count != len(word):
        print(str(count) + ": " + i, end = ", ")
        count += 1
    else:
        print(str(count) + ": " + i)

print("\n")

# count down = range(start, stop, step)
for sec in range(10, 0, -1):
    print(sec)
print("BOOOM!")
    