# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 17:26:46 2025

@author: shrut
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datadir = 'C:/Shruti/College/Semesters/Fall 2025/CSCE580/CSCE580/Exercise-height-weight/Data/'
datafile = datadir + "Data-WeightHeight.csv"
data = pd.read_csv(datafile)

data.head()
data.info()

#matplotlib inline
data.plot(x='Height (cm)', y='Weight (kg)', style='o')
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

# Imports for classification
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Get the data of interest
x = data ['Height (cm)']
y = data ['BMI Category = C1, C2, C3, C4']

# Type and shape changes
x, y = np.array(x), np.array(y)
x = x.reshape(-1,1)

# Get a subset for taining and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
print (x_train.size, x_test.size, y_train.size, y_test.size)

# Logistic Regression model
model = LogisticRegression().fit(x_train, y_train)


# Predicted values for train and test
y_pred_train = model.predict(x_train)
y_pred_test = model.predict(x_test)

# Define a function to predict error statistics
def print_stats(y_actual, y_pred):
    print("Accuracy:", accuracy_score(y_actual, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_actual, y_pred))
    print("Classification Report:\n", classification_report(y_actual, y_pred))
    
# Print for training data
print('Training Data')
print_stats(y_train, y_pred_train)

# Print for test data
print('Test Data')
print_stats(y_test, y_pred_test)


#%%

new_height = 50
predicted_class = model.predict([[new_height]])[0]
print(f"Height:{new_height} cm. Class Prediction: {predicted_class}")

new_height = 100
predicted_class = model.predict([[new_height]])[0]
print(f"Height:{new_height} cm. Class Prediction: {predicted_class}")

new_height = 150
predicted_class = model.predict([[new_height]])[0]
print(f"Height:{new_height} cm. Class Prediction: {predicted_class}")

new_height = 200
predicted_class = model.predict([[new_height]])[0]
print(f"Height:{new_height} cm. Class Prediction: {predicted_class}")

new_height = 150
predicted_class = model.predict([[new_height]])[0]
print(f"Height:{new_height} cm. Class Prediction: {predicted_class}")
