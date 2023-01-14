class PlayerCharacter:
    def __init__(self, name, age):

        # ._variableName = means the variable is private (shouldn't be changed) 
        self._name = name
        self._age = age
    
    def run(self):
        print("run")
    
    def speak(self):
        print(f"My name is {self._name}, and I am {self._age} years old")

player1 = PlayerCharacter("Yazan", 19)

print(player1.speak)