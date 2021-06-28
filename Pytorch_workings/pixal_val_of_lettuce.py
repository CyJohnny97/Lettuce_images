import numpy as np
import cv2
import pandas as pd

df = pd.read_csv('C:\\Users\\j_theocharides\\PycharmProjects\\AiCore_Lettuce\\Lettuce_images\\Merged_dataframes.csv')
print(len(df))

info_list = []
for i in range(len(df)):

    image = cv2.imread(f'C:\\Users\\j_theocharides\\PycharmProjects\\AiCore_Lettuce\\Lettuce_images\\images\\rgb\\{df["RGBImage"][i]}')
    image_2 = cv2.imread(f'C:\\Users\\j_theocharides\\PycharmProjects\\AiCore_Lettuce\\Lettuce_images\\images\\depth\\{df["DebthInformation"][i]}')
    print(df["RGBImage"][i])
    print(df["DebthInformation"][i])
    # Deciding the upper and lower RGB values for a leaf of a particular variety
    upper = df["Upper"][i]
    upper = np.array([int(upper[0:3]), int(upper[5:8]), int(upper[10:])], dtype="uint8")
    lower = df["Lower"][i]
    lower = np.array([int(lower[0:2]), int(lower[4:6]), int(lower[8:])], dtype="uint8")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Cutting out area that matches leaf color
    mask = cv2.inRange(hsv, (lower), (upper))
    cv2.imwrite('test.png', mask)
    # Overlaying mask over original image
    output = cv2.bitwise_and(image, image, mask=mask)
    # Overlaying mask over depth image to find min max depth
    output_2 = cv2.bitwise_and(image_2, image_2, mask=mask)
    gray = cv2.cvtColor(output_2, cv2.COLOR_BGR2GRAY)
    # Examing depth area withing mask for min max value
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.imwrite('test2.png', output)
    # cv2.imshow("images", np.hstack([image, output]))

    pixels = cv2.countNonZero(mask)

    ex = {
        "RGBImage": df["RGBImage"][i],
        "DebthInformation": df["DebthInformation"][i],
        "Pixels": pixels,
        "Max_val": maxVal,
    }
    info_list.append(ex)

df_1 = pd.DataFrame(info_list)
df_1.to_csv('pixel_vals.csv')