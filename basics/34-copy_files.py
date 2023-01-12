# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a dictionary
# copy2() = copy() + copies metadata (file's creation and modification times)

# Shutil module offers high-level operation on a file like a copy, create, and remote operation on the file.
import shutil

src = 'C:\\Users\\bayst\\coding\\python\\files\\test3.txt'
dst = 'C:\\Users\\bayst\\coding\\python\\basics'

# .copyfile(src, dst)
shutil.copyfile(src, dst)
