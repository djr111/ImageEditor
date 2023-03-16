from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs' # folder for unedites images
pathOut = '/editedImgs' # folder for edited images

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # sharpening, black&white
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    # contrast
    factor = 1.5
    enchancer = ImageEnhance.Contrast(edit)
    edit = enchancer.enhance(factor)


    # ADD MORE EDITS FROM DOCUMENTATION https://pillow.readthedocs.io/en/stable/
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')

    print("Job's done.")