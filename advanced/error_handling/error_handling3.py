while True:
    try:
        age = int(input("What is your age?: "))
        10 / age
    except ValueError:
        print("please enter a number")
    except ZeroDivisionError:
        print("please enter age higher than 0")
    else:
        print("thank you!")
        break
    # in the finally block, the code is executed after execute code above
    finally:
        print("ok i am finally done")