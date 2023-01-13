# OOP

class PlayerCharacter:
    membership = True
    def __init__(self, name="Anonymous", age=20):
        if (age > 18):
            self.name = name
            self.age = age
    
    def run(self):
        print("run")
        return "done"
    
    def shout(self):
        print(f"my name is {self.name}")

    # decorator
    @classmethod
    def adding_things(cls, num1, num2): # cls = stands for "class"
        return num1 + num2
    
    @staticmethod
    def substarct(num1, num2):
        return num1 - num2

player1 = PlayerCharacter("Haruto", 24)
player2 = PlayerCharacter("Yazan", 19)
player3 = PlayerCharacter()

print(player1.name)
print(player2.name)
print(player3.name)

print(player1.adding_things(2,3))
print(PlayerCharacter.adding_things(4, 9)) # @classmethod