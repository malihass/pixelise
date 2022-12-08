from PIL import Image
import os

hr_image_path = os.path.join('image_hr','hr_ks.png')

hr_image = Image.open(hr_image_path)
hr_size = hr_image.size


lr_factor = 10
lr_size = list(hr_size)
lr_size[0] = hr_size[0]//lr_factor 
lr_size[1] = hr_size[1]//lr_factor 
lr_size = tuple(lr_size)

lr_image = hr_image.resize(lr_size)
lr_image.show()
