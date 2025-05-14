import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Taking Data
data = keras.datasets.fashion_mnist

# Loading Data
(train_images, train_labels), (test_images, test_labels) = data.load_data()

# Giving the Class Names
class_name = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Cost", "Sandal",
              "Shirt", "Sneaker", "Bag", "Ankle Boot"]

train_images = train_images / 255
test_images = test_images / 255

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels)

prediction = model.predict(test_images[7])

for image in range(5):
    plt.grid(False)
    plt.imshow(test_images[image], cmap=plt.cm.binary)
    plt.xlabel("Actual Image", class_name[test_images[image]])
    plt.ylabel("Prediction", class_name[np.argmax(prediction[image])])
    plt.show()

# print(train_images[7])
# pprint(train_images[7]) # Using pprint
# # Plotting the Data
# plt.imshow(train_images[7], cmap=plt.cm.binary)
# plt.show()