# Importing Image class from PIL module
from PIL import Image
import os
# Opens a image in RGB mode

imglist = []

for (root, dirs, files) in os.walk('.', topdown=True):
    print(root)
    print(dirs)
    print(files)
    imglist.append(files)

print(imglist)

for x in imglist:
    im = Image.open(x)
    width, height = im.size
    ratio = im.size
    print(ratio)
    im1 = im.resize((256, 256))
    im1.save("test.png", format='PNG', dpi=(300, 300))
    im1.show()