import pandas as pd
import numpy as np
import json
from datetime import datetime
from sklearn.model_selection import train_test_split

with open('train_data.json', 'r') as f:
    data = json.load(f)

symbols = list(data.keys())
values_list = [value for value in data.values()]

# Extract the relevant information from each entry in the JSON data
features_list = []
target_list = []
date_format = '%Y-%m-%dT%H:%M:%SZ'

# print((values_list[0][0]['begins_at']))

for values in values_list:
    for val in values:
        if val is not None:
            dt = datetime.strptime(val['begins_at'], date_format)
            timestamp_seconds = dt.timestamp()
            features_list.append([
                timestamp_seconds,
                float(val['open_price']),
                float(val['high_price']),
                float(val['low_price']),
                val['volume']
            ])
            target_list.append(float(val['close_price']))
# print(features_list[0])
features_array = np.array(features_list)
target_array = np.array(target_list)

# Ensure that the total number of rows in features_array is divisible by the data_point_per_ticker
total_rows = features_array.shape[0]
data_point_per_ticker = 251
extra_rows = total_rows % data_point_per_ticker

if extra_rows != 0:
    features_array = features_array[:-extra_rows]
    target_array = target_array[:-extra_rows]

print("Features array shape:", features_array.shape)
print("Target array shape:", target_array.shape)

# Reshape the 2D arrays into 3D arrays with shape (10703, 251, 5) and (10703, 251, 1)
X = features_array.reshape((-1, data_point_per_ticker, 5))
y = target_array.reshape((-1, data_point_per_ticker, 1))

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

# Define the size of the validation set
validation_size = 0.2

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=validation_size, random_state=42)

print("Shape of X_train:", X_train.shape)
print("Shape of X_val:", X_val.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_val:", y_val.shape)

np.save('X_train.npy', X_train)
np.save('X_val.npy', X_val)
np.save('y_train.npy', y_train)
np.save('y_val.npy', y_val)
