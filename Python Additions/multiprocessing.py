import os
from time import perf_counter
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import multiprocessing

# Params for images
width = 800
height = 600
img_mode = 'RGB'
img_quantity = 3


def create_img(filename, img_mode: str, size=(width, height)) -> None:
    """
    Create images with some text on it and put it to the Images directory
    (creating directory if not exists)
    """
    img = Image.new(mode=img_mode, size=size, color='white')
    idraw = ImageDraw.Draw(img)
    idraw.rectangle((width / 2 - 60, height / 2 - 60, width / 2 + 120, height / 2 + 120), fill='red')
    font = ImageFont.truetype('arial.ttf', size=22)
    idraw.text((width / 2, height / 2), f'{filename}', font=font)
    # img.show() Open Each image after creation
    print(f'Image {os.path.basename(filename)} has been created. \n')
