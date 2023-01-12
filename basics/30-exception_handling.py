# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("cannot divide by 0")
except ValueError:
    print("Enter only numbers, plz")
except Exception:
    print("something went wrong.")

# if input pass all exception, executeed else statement
else:
    print(result)

# executed finally statement whether input is exception or not
finally:
    print("This line in finally statement will always execute")