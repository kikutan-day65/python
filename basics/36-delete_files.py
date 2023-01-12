import os
import shutil

# shutil.rmtree(path) = delete directory and all of contents in it 

path = 'C:\\Users\\bayst\\coding\\python\\basics\\deltest.txt'

# .remove(), .rmdir()
try:
    os.remove(path)
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("You don't have persmmion to delete")
except OSError:
    print("you cannot deletet that usin that function")
else:
    print(path + " was deleted")