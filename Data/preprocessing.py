# this is where the preprocessing happens

import pandas as pd
import numpy as np
import json

with open('Data/train_data.json', 'r') as f:
    data = json.load(f)

# convert the data to a panads dataframe
df = pd.DataFrame(data)

# convert the timestamp column to a datetime and set it as the index
df['begins_at'] = pd.to_datetime(df['begins_at'], unit='s')
df.set_index('begins_at', inplace=True)

# Remove unnecessary columns
df.drop(['interpolated', 'session', 'volume'], axis=1, inplace=True)

# Handle missing data
df.fillna(method='ffill', inplace=True)

# Normalize the data
min_vals = df.min()
max_vals = df.max()
df = (df - min_vals) / (max_vals - min_vals)

# create input and target sequences
input_seq = []
target_seq = []
seq_len = 60

for i in range(len(df) - seq_len):
    input_seq.append(df[i:i+seq_len])
    target_seq.append(df['close_price'][i+seq_len])

# convert the sequences to numpy arrays
x = np.array(input_seq)
y = np.array(target_seq)

# split the data into training and validation sets
train_size = int(len(x) * 0.8)
x_train = x[:train_size]
y_train = y[:train_size]
x_valid = x[train_size:]
y_valid = y[train_size:]

# save the data
np.save('Data/Processed/x_train.npy', x_train)
np.save('Data/Processed/y_train.npy', y_train)
np.save('Data/Processed/x_valid.npy', x_valid)
np.save('Data/Processed/y_valid.npy', y_valid)
