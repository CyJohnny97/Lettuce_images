import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Using simple regression models to predict both FreshWeightShoot and DryWeightShoot values of the model

df = pd.read_csv('Pixel_Merge.csv')

dropped_columns = ['Unnamed: 0', 'Image', 'Variety', 'RGBImage', 'DebthInformation','FreshWeightShoot', 'DryWeightShoot',
'Height', 'Diameter', 'LeafArea', 'Upper', 'Lower']

X = df.drop(dropped_columns, axis=1).values
y = df["DryWeightShoot"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X_test, X_validation, y_test, y_validation = train_test_split(X_test, y_test, test_size=0.5)

print("Number of samples in:")
print(f"    Training: {len(y_train)}")
print(f"    Validation: {len(y_validation)}")
print(f"    Testing: {len(y_test)}")

np.random.seed(2)

models = [LinearRegression(normalize=True), SVR(), DecisionTreeRegressor(splitter='random')]

for model in models:
    print(model)
    model.fit(X_train, y_train)
    train_pred = model.predict(X_train)
    valid_pred = model.predict(X_validation)
    train_loss = mean_squared_error(y_train, train_pred)
    validation_loss = mean_squared_error(y_validation, valid_pred)
    train_score = model.score(X_train, y_train)
    val_score = model.score(X_validation, y_validation)

    print(
        f"{model.__class__.__name__}: "
        f"Train Loss: {train_loss} | Validation Loss: {validation_loss} | "
    )

    print(f"Train Score: {train_score} "
          f"Val Score: {val_score} ")