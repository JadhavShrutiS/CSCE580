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
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Get the data of interest
x = data ['Height (cm)']
y = data ['Weight (kg)']

# Type and shape changes
x, y = np.array(x), np.array(y)
x = x.reshape(-1,1)

# Get a subset for taining and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
print (x_train.size, x_test.size, y_train.size, y_test.size)

# Train a linear regression mode
model = LinearRegression().fit(x_train, y_train)

# Model information
print (' Model details:')
print (' -  intercept : ', model.intercept_)
print (' -  coeff : ', model.coef_)

# Predicted values for train and test
y_pred_train = model.predict(x_train)
y_pred_test = model.predict(x_test)

# Define a function to predict error statistics
def print_stats(y_actual, y_pred):
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_actual, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_actual, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_actual, y_pred)))
    print('R^2 Score: ', r2_score(y_actual, y_pred))
    
# Print for training data
print('Training Data')
print_stats(y_train, y_pred_train)

# Print for test data
print('Test Data')
print_stats(y_test, y_pred_test)

# Visually showing the results
plt.scatter(x_test, y_test, color='black')
plt.plot(x_test, y_pred_test, color='blue', linewidth=5)
plt.xticks(())
plt.yticks(())
plt.show()

new_height = 50  # replace with your desired height
predicted_weight = model.predict([[new_height]])
print(f"Predicted weight for height {new_height} cm: {predicted_weight[0]:.2f} kg")

new_height = 100  # replace with your desired height
predicted_weight = model.predict([[new_height]])
print(f"Predicted weight for height {new_height} cm: {predicted_weight[0]:.2f} kg")

new_height = 150  # replace with your desired height
predicted_weight = model.predict([[new_height]])
print(f"Predicted weight for height {new_height} cm: {predicted_weight[0]:.2f} kg")

new_height = 170  # replace with your desired height
predicted_weight = model.predict([[new_height]])
print(f"Predicted weight for height {new_height} cm: {predicted_weight[0]:.2f} kg")

new_height = 190  # replace with your desired height
predicted_weight = model.predict([[new_height]])
print(f"Predicted weight for height {new_height} cm: {predicted_weight[0]:.2f} kg")
