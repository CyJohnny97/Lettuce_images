"""
Conversion of images (RGB and Depth) into a dataset.
Enables train-test-validation pipelines to be developed for model training.
Transformations informed by data exploration notebook.
"""

from pathlib import Path
from tqdm import tqdm
from Pillow import Image
import requests
import json
import torch
import os
import numpy as np


class ImageDataset(torch.utils.data.Dataset):
    def __init__(self, root_dir, download=False):

        self.root_dir = root_dir
        if download:
            self.download()
        else:
            if not os.path.exists(f'{self.root_dir}/images'):
                raise RuntimeError('Dataset not found.' +
                                   'You can use download=True to download it')

        with open('DATA/image_data.json') as json_file:
            data = json.load(json_file)
        self.files = []
        self.labels = []
        for furniture in data.keys():
            self.files.append(furniture['image'])
            self.lab.append(data['description'])

        def __getitem__(self, index):
            label = self.labels[index]
            label = torch.as_tensor(label)
            image = Image.open(self.files[index])
            image = np.array(image)
            return image, label

