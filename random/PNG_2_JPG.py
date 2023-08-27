import os
import glob
import pathlib

from PIL import Image

photoDir = r'C:\Users\andolson\Documents\WORKING\WildFire\Tensorflow_Images\firebreak_images'
data_dir = pathlib.Path(photoDir)
print(data_dir)

for jpeg_fp in data_dir.glob('*/*.jpeg'):
    im = Image.open(jpeg_fp)
    rgb_im = im.convert('RGB')
    jpg_fp = os.path.splitext(jpeg_fp)[0]
    rgb_im.save(f"{jpg_fp}.jpg")
    os.rename(newDIR, base + '.jpg')

'''
import os
import glob

from PIL import Image

for png_fp in data_dir.glob("*.png"):
    im = Image.open(png_fp)
    rgb_im = im.convert('RGB')
    jpg_fp = os.path.splitext(png_fp)[0]
    rgb_im.save(f"{jpg_fp}.jpg")
'''