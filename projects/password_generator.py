username = input("Enter your name: ")
password = input("Enter your password: ")

passwordLen = len(password)
hiddenPassword = '*' * passwordLen

print(f"{username}, your password, {hiddenPassword} is {passwordLen} letters long")
