# logical operators (and, or, not) = used to check if two or more conditional statement is true/false

temp = int(input("What is the temperature outside?: "))

# and/or operator
if temp >= 0 and temp <= 30:
    print("the temperature is good today")
    print("Go, outside.")
elif temp < 0 or temp > 30:
    print("the temperature is bad today")
    print("Stay inside.")


# not operator
score = int(input("What is your score of the exam?: "))
if not(score >= 50 and score <= 100):
    print("You fail.")
elif not(score < 50):
    print("you pass.")