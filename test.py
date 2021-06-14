import requests

# Change this with your URL
url = f'https://aicore-lettuce-project.s3.eu-central-1.amazonaws.com/FirstTrainingData/RGB_100.png'
response = requests.get(url)
print(response.status_code)
with open('image3.png', 'wb') as f:
    f.write(response.content)
