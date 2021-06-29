import pandas as pd

# Adding the max and min RGB values of the types of lettuces to datasets

df0 = pd.read_csv('Image_dataset.csv')
df1 = pd.read_csv('Lettuce_RGB_values.csv')

df2 = pd.merge(df0, df1, how='outer')

print(df2.head())

df2.to_csv('Merged_dataframes.csv')

