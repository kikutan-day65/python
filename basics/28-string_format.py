# str.format() = optional method that gives users
#                more control when displaying output


animal = "dog"
item = "moon"

print("The " + animal + " jumped over the " + item)

# same output above, used placeholder{}
print("The {} jumped over the {}".format(animal, item))

print("dobry den, {name}! do u wanna go to the {place}?".format(name="Haruto", place="restaurant"))


book = "Magic"
print("my favorite book is {:20}. What about you?".format(book))

# align center in 20 spaces
print("my favorite book is {:^20}. What about you?".format(book))

# align left in 20 spaces
print("my favorite book is {:<20}. What about you?".format(book))

# align right in 20 spaces
print("my favorite book is {:>20}. What about you?".format(book))


PI = 3.14159
# displays only two digits
print("The number PI is {:.2}".format(PI))