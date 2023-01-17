while True:
    try:
        age = int(input("What is your age?: "))
        10 / age

        # tells an error with your arbitrary comments
        raise ValueError("hey cut it out")
    except ZeroDivisionError:
        print("please enter age higher than 0")
    else:
        print("thank you!")
        break
    finally:
        print("ok i am finally done")