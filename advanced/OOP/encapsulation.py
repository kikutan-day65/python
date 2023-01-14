# encapsulation = the binding data (attributes) and functions (methods) that manipulate that data

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def run(self):
        print("run")
    
    def speak(self):
        print(f"My name is {self.name}, and I am {self.age} years old")

player1 = PlayerCharacter("Haruto", 25)
player1.speak()

print(player1.name)
print(player1.age)

player2 = {"name": "Haruto", "age": 25}
print(player2["name"])
print(player2["age"])