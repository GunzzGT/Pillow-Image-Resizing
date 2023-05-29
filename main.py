from PIL import Image
import os

#r"C:\Users\gunaw\Pictures"

directory_name = "C:\\Users\\gunaw\\Pictures"
file_list = []
for (root,dirs,files) in os.walk(directory_name):
    for file in files:
        file_list.append(os.path.join(root,file))

for f in file_list:
    print(f)

"""
#NOTES
testarr1 = os.listdir()
print(testarr1)
#list every files and sub-directory on main directory

testarr2 = [os.path.abspath(x) for x in os.listdir()]
print (testarr2)
#list every files and sub-directory with its directory, works weirdly if specify which directory on listdir

cwd = ""
onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
print(onlyfiles)
#list every files with its directory

for x in imglist:
    im = Image.open(x)
    width, height = im.size
    ratio = im.size
    print(ratio)
    im1 = im.resize((256, 256))
    im1.save("test.png", format='PNG', dpi=(300, 300))
    im1.show()
"""
