class User(object):
    def __init__(self, email):
        self.email = email
        
    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"attacking with power of {self.power}")


# introspection = ability to determine the type of object at run time
wizard1 = Wizard("Merlin", 60, "haruto@outlook.com")

# dir() = returns all properties and methods of the specified object, without the values.
print(dir(wizard1))    