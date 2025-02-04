"""
    KNN on Iris Data
"""
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Loading Datasets
iris = datasets.load_iris()
features = iris.data[25:]
labels = iris.target[25:]

clf = KNeighborsClassifier()
clf.fit(features, labels)

for _ in range(101):
	prediction = clf.predict([np.random.randint(1, 10, size=4)])
	print(prediction, end="")

"""
    KNN on Car Data
"""
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import matplotlib.pyplot as plt

# Reading Data
data = pd.read_csv("car.data")

le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint  = le.fit_transform(list(data["maint"]))
doors  = le.fit_transform(list(data["doors"]))
person = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls    = le.fit_transform(list(data["class"]))

predict = "class"

x = list(zip(buying, maint, doors, person, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(f"accuracy is :- {acc}")
#
# predicted = model.predict(x_test)
# names = ["unacc", "acc", "good", "vgood"]
#
# for num in range(len(predicted)):
# 	print(f"Predicted :- {names[predicted[num]]} Data :- {x_test[num]} Actual :- {names[y_test[num]]}")

y_predict = model.predict(x_test)
# Plotting as Graph
fig, ax = plt.subplots()
ax.scatter(y_test, y_predict)
ax.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'k--', lw=4)
ax.set_xlabel('Actual')
ax.set_ylabel('Predicted')
plt.show()
