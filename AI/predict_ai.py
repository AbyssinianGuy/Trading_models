from tensorflow.python.keras.models import load_model
import numpy as np

# Load the model
model = load_model('model.h5')

# Load the data
X_val = np.load('../Data/Processed/X_val.npy')

# Make predictions
predictions = model.predict(X_val)
print(predictions)
print(predictions.shape)
