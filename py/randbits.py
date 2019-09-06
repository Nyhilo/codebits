from PIL import Image
from random import randint, random

size = 1000

img = Image.new( 'RGB', (size,size), "black") # Create a new black image
pixels = img.load() # Create the pixel map
for i in range(img.size[0]):    # For every pixel:
    for j in range(img.size[1]):
        greyscaleRange = 1  # 1 is binary, 255 is full greyscale range
        bit = randint(0,255)
        pixels[i,j] = (randint(0,255), randint(0,255), randint(0,255)) # RGB values

img.show()