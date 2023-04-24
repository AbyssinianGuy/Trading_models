# This is where the deep learning magic happens

import numpy as np
from keras.layers import Bidirectional, Dropout, LSTM, Dense
from tensorflow.python.keras.models import Sequential, load_model

# Load the data
X_train = np.load('../Data/Processed/X_train.npy')
y_train = np.load('../Data/Processed/y_train.npy')
X_val = np.load('../Data/Processed/X_val.npy')
y_val = np.load('../Data/Processed/y_val.npy')

# Modify the target array shapes
# y_train = y_train
# y_val = y_val

# Define the model
model = Sequential([
    Bidirectional(LSTM(128, input_shape=(250, 5), return_sequences=True)),
    Dropout(0.2),
    LSTM(64, return_sequences=True),
    Dropout(0.2),
    LSTM(32),
    Dropout(0.2),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])  # mean_absolute_error

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

# Evaluate the model
eval_results = model.evaluate(X_val, y_val)

mse, mae = eval_results

print("Mean squared error:", mse)
print("Mean absolute error:", mae)

# Save the model
model.save('model-lstm')
#
# print("Model saved to disk")

# Load the model
# model = load_model('model.h5')

# Make prediction
# predictions = model.predict(X_val)
# print(predictions)
