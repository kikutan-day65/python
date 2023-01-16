# decorator

# decorator pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("**************")
        func(*args, **kwargs)
        print("**************")
    return wrap_func

@my_decorator
def hello():
    print("helloooooo")

@my_decorator
def bye():
    print("see you")

hello()
bye()

# hello2 = my_decorator(hello)
# my_decorator(hello)()
# hello2()