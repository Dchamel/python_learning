import os
from time import perf_counter
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import multiprocessing

# Params for images
width = 800
height = 600
img_mode = 'RGB'
img_quantity = 10


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
    img.save(f'images/{filename}')


def create_thmb(filename: list, size=(100, 100)) -> None:
    """Create thumbs from image dir and save them to thumbs dir"""
    img = Image.open(f'images/{filename}')
    img = img.filter(ImageFilter.GaussianBlur())
    img.thumbnail(size)
    img.save(f'images/thumbs/{filename}')
    print(f'File {filename} done.')


if __name__ == '__main__':
    t1 = perf_counter()

    # create pool of images
    if not os.path.exists('images'):
        os.makedirs('images')

        process_list = [multiprocessing.Process(
            target=create_img,
            args=[f'{i}.jpg', img_mode, (width, height)]
        ) for i in range(1, img_quantity + 1)]

        # start all processes
        for process in process_list:
            process.start()
        # wait to finish all processes
        for process in process_list:
            process.join()

        all_files = os.listdir('images/')
        if not os.path.exists('images/thumbs'):
            os.makedirs('images/thumbs')
            print(all_files)
            for file in all_files:
                process_list = [multiprocessing.Process(
                    target=create_thmb, args=[file]
                )]
            # start and wait all processes
            for process in process_list:
                process.start()
            for process in process_list:
                process.join()

    t2 = perf_counter()
    print(f'Working time {t2 - t1:.2f} sec')
