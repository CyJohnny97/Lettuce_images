# import boto3
# import os
#
#
# def download_dir(client, resource, dist, local='/tmp', bucket='your_bucket'):
#     paginator = client.get_paginator('list_objects')
#     for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
#         if result.get('CommonPrefixes') is not None:
#             for subdir in result.get('CommonPrefixes'):
#                 download_dir(client, resource, subdir.get('Prefix'), local, bucket)
#         for file in result.get('Contents', []):
#             dest_pathname = os.path.join(local, file.get('AKIASZT3ISRAQH6F7MHM'))
#             if not os.path.exists(os.path.dirname(dest_pathname)):
#                 os.makedirs(os.path.dirname(dest_pathname))
#             resource.meta.client.download_file(bucket, file.get('AKIASZT3ISRAQH6F7MHM'), dest_pathname)
#
#
# def _start():
#     client = boto3.client('s3')
#     resource = boto3.resource('s3')
#     download_dir(client, resource, 'clientconf/', '/tmp', bucket='aicore-lettuce-bucket')

import os
import boto3

ACCESS_KEY = 'AKIASZT3ISRAQH6F7MHM'
SECRET_KEY = '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'

client_s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key= SECRET_KEY
)

client_s3.download_file('aicore-lettuce-bucket', 'RGB_1.png', os.path.join('./images/', 'new_images.png'))
