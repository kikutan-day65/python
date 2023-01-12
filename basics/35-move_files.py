import os


# set a path correctly
src = 'C:\\Users\\bayst\\coding\\python\\file\\test3.txt'
dst = 'C:\\Users\\bayst\\coding\\python\\basics\\moved.txt'


try:
    if os.path.exists(dst):
        print("there's already a file there")
    else:
        os.replace(src, dst)
        print(src + " was moved")
except FileNotFoundError:
    print(src + " was not found")

