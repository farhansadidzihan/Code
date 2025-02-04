"""
    This if for practising Machine Learning with Python
"""


# import matplotlib.pyplot as plt
# from wordcloud import WordCloud

# text = "your text goes here"

# wordcloud = WordCloud(width = 800, height = 800, 
#                 background_color ='white', 
#                 stopwords = stopwords, 
#                 min_font_size = 10).generate(text)

# # Display the generated image:
# plt.figure(figsize = (8, 8), facecolor = None) 
# plt.imshow(wordcloud) 
# plt.axis("off") 
# plt.tight_layout(pad = 0) 

# plt.show()


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(X, y)
# Pipeline(steps=[('standardscaler', StandardScaler()), ('svc', SVC(gamma='auto'))])
print(clf.predict([[-0.8, -1]]))

# Load the iris dataset
df = pd.read_csv("iris.data")

# Split the data into features and labels
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
 
# Create an SVM model and train it
model = SVC()
model.fit(X_train, y_train)

# Evaluate the model on the test data
accuracy = model.score(X_test, y_test)

print('Test accuracy:', accuracy)
