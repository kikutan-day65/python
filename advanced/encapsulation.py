class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

player1 = PlayerCharacter("Haruto", 25)
print(player1.name)
print(player1.age)

# works same as above
player2 = {"name": "HARUTO", "age": 30}
print(player2["name"])
print(player2["age"])