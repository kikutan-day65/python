import random

# generating random integer number
x = random.randint(1, 6)
print(x)

# generating random floating number
y = random.random()
print(y)

# .choice() = chooses somrthing in the list
myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
print(z)

# .shuffle() = shuffles the elemnt in the list 
cards = ["A",2,3,4,5,6,7,8,9,"J","Q", "K"]
random.shuffle(cards)

print(cards)