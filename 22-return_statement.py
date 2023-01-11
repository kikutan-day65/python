# return statement = functions send python values/pbjects back to the caller.
#                    these values/objects are known as the function's return value

def multiply(num1, num2):
    return num1 * num2

answer = multiply(6, 8)
print(answer)


number1 = int(input("Enter a first number: "))
number2 = int(input("Enter a second number: "))

answer = multiply(number1, number2)
print(answer)