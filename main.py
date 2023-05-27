# Importing Image class from PIL module
from PIL import Image
import io
# Opens a image in RGB mode
im = Image.open(r"C:\Users\gunaw\Pictures\ARMSTROOOOOOOOOOOOONG.jpg")

width, height = im.size

ratio = im.size
print(ratio)

im1 = im.resize((256,256))
im1.save("test.png", format='PNG', dpi=(300, 300))
im1.show()