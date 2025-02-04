import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# || Reading the csv file ||
housing = pd.read_csv("data.csv")

# || Train & Test Data Splitting ||
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

housing_X = housing.data[:, np.newaxis, 2]

housing_X_train = housing_X[:-400]
housing_X_test  = housing_X[-107:]

housing_y_train = housing.target[:-400]
housing_y_test  = housing.target[-107:]

model = LinearRegression()
model.fit(housing_X_train, housing_y_train)

housing_y_predicted = model.predict(housing_X_test)


plt.scatter(housing_X_test, housing_y_test, color="red")
plt.plot(housing_X_test, housing_y_predicted, color="blue")
plt.show()