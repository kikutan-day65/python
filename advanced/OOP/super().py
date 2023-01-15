class User(object):
    def __init__(self, email):
        self.email = email
        
    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name, power, email):
        # super() refers to the class above --> User
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"attacking with power of {self.power}")


wizard1 = Wizard("Merlin", 60, "haruto@outlook.com")
print(wizard1.email)
    