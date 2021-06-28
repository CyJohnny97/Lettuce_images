import pandas as pd

df0 = pd.read_csv('Merged_dataframes.csv')
df1 = pd.read_csv('C:\\Users\\j_theocharides\\PycharmProjects\\AiCore_Lettuce\\Lettuce_images\\Pytorch_workings\\pixel_vals.csv')

df2 = pd.merge(df0, df1, how='outer')

print(df2.head())

df2.to_csv('Pixel_Merge.csv')
