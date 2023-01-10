# if statement = a block of code that will execute of its condition id true
age = int(input("How old are you?: "))

if age == 100:
    print("You're a century old!")
elif age >= 18:
    print("You're an adult.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You're a child.")