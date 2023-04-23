import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Load data
with open('train_data.json', 'r') as f:
    data = json.load(f)

# Preprocess data
values_list = [value for values in data.values() for value in values]
data_points = np.array([[float(val['open_price']), float(val['close_price']), float(val['high_price']),
                         float(val['low_price']), float(val['volume'])] for val in values_list])

# Scale the features
scaler = MinMaxScaler()
data_points = scaler.fit_transform(data_points)

# Create sequences using sliding window approach
sequence_length = 251
step_size = 5  # How many steps to take between each sequence (1 = no overlap)
sequences = []
for i in range(0, len(data_points) - sequence_length, step_size):
    sequences.append(data_points[i:i + sequence_length])

sequences = np.array(sequences)

# Split data into training and validation sets
train_size = int(0.8 * len(sequences))
X_train, X_val = sequences[:train_size, :-1], sequences[train_size:, :-1]
y_train, y_val = sequences[:train_size, -1, 1], sequences[train_size:, -1, 1]  # Assuming target is close price

# Reshape target arrays
y_train = y_train.reshape(-1, 1)
y_val = y_val.reshape(-1, 1)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_val shape:", X_val.shape)
print("y_val shape:", y_val.shape)

# Save the data
np.save('Processed/X_train.npy', X_train)
np.save('Processed/y_train.npy', y_train)
np.save('Processed/X_val.npy', X_val)
np.save('Processed/y_val.npy', y_val)

print("Data saved to disk")
