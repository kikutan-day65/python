#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Alex", 2)
cat2 = Cat("Mike", 12)
cat3 = Cat("Ron", 5)


# 2 Create a function that finds the oldest cat
def oldest(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {oldest(cat1.age, cat2.age, cat3.age)} years old.")