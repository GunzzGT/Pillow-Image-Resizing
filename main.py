#from PIL import Image
import os

# r"C:\Users\gunaw\Pictures"

directory_name = "C:\\Users\\gunaw\\Pictures"
file_list = []
for (root, dirs, files) in os.walk(directory_name):
    for file in files:
        file_list.append(os.path.join(root, file))

for f in file_list:
    print(f)



#in conclusion r"{}".format(input) would be the safest option here

"""
# NOTES

# on directory files reading

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
"""

# on file reading

arr = []
test = r"C:\\Users\\gunaw\\Pictures"
arr.append(test)
print(test)
print(repr(test))
# this prints the string as is, no need \\ after read as raw with r"", string will be stored with \\\\ (four \)
test = "C:\\Users\\gunaw\\Pictures"
arr.append(test)
print(test)
print(repr(test))
# this is ok number 1
test = r"C:\Users\gunaw\Pictures"
arr.append(test)
print(test)
print(repr(test))
# this is ok number 2
test = r"{}".format("C:\\Users\\gunaw\\Pictures")
arr.append(test)
print(test)
print(repr(test))
# this is ok number 3, r"{}".format removes the \ or backslash or escape character and ignores it
test = r"{}".format(r"C:\Users\gunaw\Pictures")
arr.append(test)
print(test)
print(repr(test))
# this is ok number 4, r"{}".format still keeps the \ or backslash not as escape character
test = r"{}".format("C:\\Users\gunaw\Pictures")
arr.append(test)
print(test)
print(repr(test))
# this is ok number 5 \u is reserved for unicode, otherwise this can work too, read https://python-reference.readthedocs.io/en/latest/docs/str/escapes.html for more
print(arr)

"""
for x in imglist:
    im = Image.open(x)
    width, height = im.size
    ratio = im.size
    print(ratio)
    im1 = im.resize((256, 256))
    im1.save("test.png", format='PNG', dpi=(300, 300))
    im1.show()
"""
