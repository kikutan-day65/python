# str.format() = optional method that gives users
#                more control when displaying output


animal = "dog"
item = "moon"

print("The " + animal + " jumped over the " + item)

# same output above, used placeholder{}
print("The {} jumped over the {}".format(animal, item))

print("dobry den, {name}! do u wanna go to the {place}?".format(name="Haruto", place="restaurant"))