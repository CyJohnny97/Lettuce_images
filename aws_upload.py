"""
Upload images to S3 bucket
Allows access from any PC
Assumes AWS already to configured
"""

import boto3
from PIL import Image
import requests
import os
from io import BytesIO

def upload_to_aws(file, bucket, saved_location):
    """
    Uploads a file to the requested AWS S3 bucket
    :param file: file to upload
    :param bucket: name of the bucket, default 'aicore-akirby'
    :param saved_location: name of the file and folder in the bucket needs to be set
    :return: none
    """
    s3 = boto3.client('s3')
    try:
        upload = s3.upload_file(file, bucket, saved_location)
    # The function could be used for files on drive or image objects
    # upload_file raises a value error if the file is not string
    # In this case the alternative upload_fileobj is used
    except ValueError:
        upload = s3.upload_fileobj(file, bucket, saved_location)
    if upload is True:
        return "{} successfully uploaded to {} bucket".format(file, bucket)
    else:
        return "Failure to upload {} to {} bucket".format(file, bucket)


path = 'images//rgb//RGB_1.png'
img = Image.open(path)

# Create a name
name = path[-9:]

# Create an object in memory, aws needs a file to upload
mem_obj = BytesIO()
img.save(mem_obj, format=img.format)
mem_obj.seek(0)

# Store in aws bucket
upload_to_aws(mem_obj, 'aicore-lettuce-project', name)
