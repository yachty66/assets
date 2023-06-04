import os
from PIL import Image

images_female_folder = "images_Females"
new_size = (256, 256)

for filename in os.listdir(images_female_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(images_female_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize(new_size)
        img_resized.save(img_path)
