import os
import cv2
from PIL import Image

dir = './Alpha_Image/train/'

def png_to_jpg(png_path, target_img):
    fill_color = None
    img = target_img
    jpg_path = png_path[:-4]+'.jpg'

    if img.mode in ('RGBA', 'LA'):
        background = Image.new(img.mode[:-1], img.size, fill_color)
        background.paste(img, img.split()[-1])
        img = background

    img.save(jpg_path, 'JPEG')

for sub in os.listdir(dir):
    sub_path = dir + sub

    for image in os.listdir(sub_path):
        image_path = sub_path + "/" + image
        print(image)

        imgP = Image.open(image_path)
        #imgP = cv2.imread(image_path, cv2.IMREAD_COLOR)
        png_to_jpg(image_path, imgP)