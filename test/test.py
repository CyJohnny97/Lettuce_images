import requests
import os
# Change this with your URL
for file in os.listdir(r'C:\Users\j_theocharides\PycharmProjects\AiCore_Lettuce\Lettuce_images\images\depth'):
    print(file)
    url = f'https://aicore-lettuce-project.s3.eu-central-1.amazonaws.com/FirstTrainingData/{file}'
    response = requests.get(url)
    print(response.status_code)
    with open(f'{file}', 'wb') as f:
        f.write(response.content)

for file in os.listdir(r'C:\Users\j_theocharides\PycharmProjects\AiCore_Lettuce\Lettuce_images\images\rgb'):
    print(file)
    url = f'https://aicore-lettuce-project.s3.eu-central-1.amazonaws.com/FirstTrainingData/{file}'
    response = requests.get(url)
    print(response.status_code)
    with open(f'{file}', 'wb') as f:
        f.write(response.content)
