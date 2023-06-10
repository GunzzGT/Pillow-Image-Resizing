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


def crop(img, rat, left, right, top, bottom, res, fmt):
    old_im = Image.open(img)
    width, height = old_im.size
    old_ratio = old_im.size
    # print(old_ratio)
    new_ratio = rat
    # print(new_ratio)
    new_im = old_im.resize(res)

    size_l = left * width
    size_r = right * width
    size_t = top * height
    size_b = bottom * height

    new_im = old_im.crop((left, top, right, bottom))
    new_im = old_im.resize(new_ratio)
    new_im.save((img + "new"), format=fmt, dpi=res)
    new_im.show()
