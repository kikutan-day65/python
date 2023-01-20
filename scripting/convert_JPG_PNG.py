"""
command line:
                    [arg1]  [arg2]
>>> py convert_JPG_PNG.py pokedex\\ new\\

"""
import sys
import os
from PIL import Image

# grab firste and second argument
img_folder = sys.argv[1]
new_folder = sys.argv[2]

# check if new\ exists, if not create
isExist = os.path.exists(new_folder)
if not isExist:
    os.makedirs(new_folder)

# loop through pokedex,
# convert images to PNG
# save them to new folder

for filename in os.listdir(img_folder):
    img = Image.open(f"{img_folder}{filename}")
    #splittext() returns tuples of splitted text
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)
    img.save(f"{new_folder}{clean_name}.png", "png")
