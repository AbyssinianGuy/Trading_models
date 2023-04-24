# This is where the deep learning magic happens

import numpy as np
from keras.layers import Bidirectional, Dropout, LSTM, Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.python.keras.models import Sequential, load_model

# Load the data
X_train = np.load('../Data/Processed/X_train.npy')
y_train = np.load('../Data/Processed/y_train.npy')
X_val = np.load('../Data/Processed/X_val.npy')
y_val = np.load('../Data/Processed/y_val.npy')

# Define the model
model = Sequential([
    Bidirectional(LSTM(128, input_shape=(250, 5), return_sequences=True, activation='relu')),
    Dropout(0.2),
    LSTM(64, return_sequences=True, activation='relu'),
    Dropout(0.2),
    LSTM(32, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Define early stopping and model checkpoint callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model_checkpoint = ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True)

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val),
          callbacks=[early_stopping, model_checkpoint])

# Load the best model
best_model = load_model('best_model.h5')

# Evaluate the best model
eval_results = best_model.evaluate(X_val, y_val)

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
