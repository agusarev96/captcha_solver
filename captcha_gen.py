import random
from captcha.image import ImageCaptcha
import string

# string.ascii_uppercase
# string.digits
# !~
ALL_SYMBOLS = string.ascii_uppercase# + string.digits

def gen_captcha_text(length=4):

    symbols_list = []
    for _ in range(length):
        symbols_list.append(random.choice(ALL_SYMBOLS))

    return "".join(symbols_list)


# Create an image instance of the given size
image = ImageCaptcha(width = 280, height = 90)

for _ in range(10000):
    # Image captcha text
    captcha_text = gen_captcha_text(length=4)
     
    # generate the image of the given text
    data = image.generate(captcha_text)  

    # write the image on the given file and save it
    image.write(captcha_text, f'captcha_images/{captcha_text}.png')