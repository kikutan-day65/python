# for loop = a statement that will execute its block of code
#            a limited amount of times


# count up
for i in range(10):
    print(i)


# count up between 50 and 100
for i in range(50, 100 + 1):
    print(i)


# show even numbers between 0 and 100
for i in range(0,100 + 1, 2):
    print(i)


# show each letter of a string
word = "pneumonoultramicroscopicsilicovolcanoconiosis"
count = 1

for i in word:
    print(str(count) + ": " + i)
    count += 1