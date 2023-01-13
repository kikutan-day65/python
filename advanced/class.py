# OOP

class PlayerCharacter:
    def __init__(self, name, age):
        # creating an attribute and set what parameter will be assigned
        # self refers to a variable that coders created (player1, player2)
        self.name = name
        self.age = age
    
    def run(self):
        print("run")
        return "done"

# instances
player1 = PlayerCharacter("Haruto", 24)
player2 = PlayerCharacter("Yazan", 19)

print(player1) # shows where the object player1 is stored at the memory
print(player1.name)
print(player1.age)
print(player1.run())

print(player2) # shows where the object player2 is stored at the memory
print(player2.name)
print(player2.age)
print(player2.run())