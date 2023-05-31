from PIL import Image

def resize(img, rat, res, fmt):
    old_im = Image.open(img)
    old_ratio = old_im.size
    # print(old_ratio)
    new_ratio = rat
    # print(new_ratio)
    new_im = old_im.resize(new_ratio)
    new_im.save((img + "new"), format=fmt, dpi=res)
    new_im.show()


def crop(img, siz, pos, res, fmt):
    pass