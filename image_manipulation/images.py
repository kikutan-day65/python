from PIL import Image, ImageFilter

img = Image.open(".\pokedex\pikachu.jpg")

# shows image's property
print(img)

# shows coloring mode
print(img.mode)

# blur image
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png") # save the image

# smooth image
smoothed_image= img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png", "png") # only png flie is supported to the ImageFilter

"""
# check the diffences
img1 = "C:\\Users\\bayst\\coding\\python\\scripting\\blur.png"
img2 = "C:\\Users\\bayst\\coding\\python\\scripting\\smooth.png"

if img1 == img2:
    print("its the same")
else:
    print("not the same")
"""

# convert to grey scale
converted_img = img.convert('L')
converted_img.save("grey.png", "png")

# shows the image
# converted_img.show()

# rotates the image
crooked_img = filtered_img.rotate(180)
crooked_img.save("crooked.png", "png")
# crooked_img.show()

# resize the image
resized_img = filtered_img.resize((1980, 1200))
# resized_img.show()

# crop the image
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("cropped.png", "png")
# region.show()

astro_img = Image.open(".\\image\\astro.jpg")

# check the size of the image
print("image size: " + str(astro_img.size))

# resize the image as a thumbnail, image isn't be squashed. useful for creating profile image
astro_img.thumbnail((400, 400))
astro_img.save("thumnail.jpg")
print("image size: " + str(astro_img.size))
