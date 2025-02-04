"""
    Students Performance Predicting Model
"""
import numpy as np
# import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

diabates = datasets.load_diabetes()

diabates_X = diabates.data[:, np.newaxis, 2]

diabates_X_train = diabates_X[:-30]
diabates_X_test  = diabates_X[-30:]

diabates_y_train = diabates.target[:-30]
diabates_y_test  = diabates.target[-30:]

model = linear_model.LinearRegression()
model.fit(diabates_X_train, diabates_y_train)

diabates_y_predicted = model.predict(diabates_X_test)

print(mean_squared_error(diabates_y_test, diabates_y_predicted))

plt.scatter(diabates_X_test, diabates_y_test, color="red")
plt.plot(diabates_X_test, diabates_y_predicted, color="blue")
plt.show()

"""
    Students Performance Predicting Model
"""
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
from matplotlib import style
import pickle

# Reading Data
data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
"""
best = 0
for _ in range(50):
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)

    if acc > best:
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
"""

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

predictions = linear.predict(x_test)

# for x in range(len(predictions)):
#     print(predictions[x], x_test[x], y_test[x])

style.use("ggplot")
pyplot.scatter(data["absences"], data["failures"])
pyplot.xlabel("Absences")
pyplot.ylabel("Failures")
pyplot.show()


# # Load the necessary libraries
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
#
# # Load the iris dataset
# df = pd.read_csv('iris.csv')
#
# # Split the data into features and labels
# X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
# y = df['species']
#
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Create an SVM model and train it
# model = SVC()
# model.fit(X_train, y_train)
#
# # Evaluate the model on the test data
# accuracy = model.score(X_test, y_test)
#
# print('Test accuracy:', accuracy)
