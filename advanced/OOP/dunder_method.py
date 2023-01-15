# dunder methods = methods that allow instances of a class to 
#                  interact with the built-in functions and operators of the language.

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "Yoyo",
            "has_pets": False
        }

    def __str__(self):
        return f"{self.color}"
    
    def __len__(self):
        return 5
    
    # def __del__(self):
    #     print("deleted!")
    
    def __call__(self):
        return("yes??")
    
    def __detitem__(self, i):
        return self.my_dict[i]


action_figure = Toy("Red", 0)
print(action_figure.__str__())
print(str(action_figure))

print(len(action_figure))
# del action_figure

# __call__
print(action_figure())

# __getitem__
print(action_figure["name"]) # TypeError occurs