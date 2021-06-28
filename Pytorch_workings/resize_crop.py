from PIL import Image
import pandas as pd

df = pd.read_csv(r'C:\Users\j_theocharides\PycharmProjects\AiCore_Lettuce\Lettuce_images\Image_dataset.csv')

cat = df['Variety'].to_list()
image = df["RGBImage"].to_list()

for i, im in enumerate(image):
    ca = cat[i]
    im_2 = Image.open("C:\\Users\\j_theocharides\\PycharmProjects\\AiCore_Lettuce\\Lettuce_images\\images\\rgb\\" + im)
    width, height = im_2.size
    left = int((width - 960)/2)
    top = int((height - 270*2)/2)
    right = int((width + 960)/2)
    bottom = int((height + 270*2)/2)
    print(im, width, height, left, top, right, bottom)
    im_out = im_2.crop((left, top, right, bottom))
    save_file = 'C:\\Users\\j_theocharides\\PycharmProjects\\AiCore_Lettuce\\Lettuce_images\\Pytorch_workings\\lettuce_data\\train\\' + ca + '\\' + im
    im_out.save(save_file, format='png')
