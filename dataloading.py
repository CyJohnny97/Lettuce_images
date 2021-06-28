"""
Conversion of images (RGB and Depth) into a dataset.
Enables train-test-validation pipelines to be developed for model training.
Transformations informed by data exploration notebook.
"""


import os
import pandas as pd
import json
from PIL import Image
from matplotlib import pyplot as plt

cwd = os.getcwd()
rgb_path = os.path.join(cwd, 'images', 'rgb', 'RGB_1.png')

rgb_img = Image.open(rgb_path)

plt.imshow(rgb_img)
plt.show()

# Let's check the depth image
depth_path = os.path.join(cwd,'images', 'depth','Debth_1.png' )

depth_img = Image.open(depth_path)

# Example depth image
plt.imshow(depth_img)
plt.show()

# Depth image looks like a promising path to reduce the image size to focus on the key features.

# Lets try a larger lettuce as well
depth_img_lrg = Image.open(os.path.join(cwd, 'images', 'depth', 'Debth_346.png' ))

plt.imshow(depth_img_lrg)
plt.show()

# A little bit trickier, because the lettuce extends over the crate. Lets look at different options for cropping

rgb_img_cropped = rgb_img.crop((600, 200, 1600, 1000))
plt.imshow(rgb_img_cropped)
plt.show()


image_info = pd.read_json(os.path.join(cwd, 'images', 'labels_latest.json'))

image_info.head()

# Open json file with all feature and target information
with open(os.path.join(cwd, 'images', 'labels_latest.json'), 'r') as f:
    image_info2 = json.loads(f.read())

# Confirm success
print(image_info2['Measurements'].keys())

# Check there are no duplicates
if len(image_info2['Measurements'].keys()) == len(set(image_info2['Measurements'].keys())):
    print('NO DUPLICATES!')
else:
    print('We are screwed...')

image_list = image_info2['Measurements'].keys()

for image in image_list:
    print(image_info2['Measurements'][image])
    break

data = pd.DataFrame(image_info2['Measurements'])
print(data.T.head())

data.T.to_csv('Image_dataset.csv')

