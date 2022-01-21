from PIL import Image
import PIL
im = Image.open(".\captcha.gif")
im = im.convert("P")
im2 = Image.new("P",im.size,255)

temp = {}

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        temp[pix] = pix
        if pix == 220 or pix == 227: # these are the numbers to get_
            im2.putpixel((y,x),0)

im2.save("output.gif")
