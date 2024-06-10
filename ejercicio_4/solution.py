import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data_customer_classification.csv')

# Preprocess the data
data['trans_date'] = pd.to_datetime(data['trans_date'])
data['year'] = data['trans_date'].dt.year

# Calculate total spending, maximum spending, and shopping frequency
customer_stats = data.groupby('customer_id').agg({
    'tran_amount': ['sum', 'max', 'count']
}).reset_index()

# Rename columns
customer_stats.columns = ['customer_id', 'total_spending', 'max_spending', 'shopping_frequency']

# Categorize customers into low, medium, and high value based on total spending
bins = [0, 100, 1000, np.inf]
labels = ['low', 'medium', 'high']
customer_stats['category'] = pd.cut(customer_stats['total_spending'], bins=bins, labels=labels)

# Convert categorical labels to numerical
customer_stats['category'] = customer_stats['category'].map({'low': 0, 'medium': 1, 'high': 2})

# Prepare the data for training
X = customer_stats[['total_spending', 'max_spending', 'shopping_frequency']].values
y = customer_stats['category'].values

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the model
model = Sequential([
    Dense(64, input_dim=X_train.shape[1], activation='relu'),
    Dropout(0.5),
    Dense(32, activation='relu'),
    Dropout(0.5),
    Dense(16, activation='relu'),
    Dense(3, activation='softmax')  # 3 classes for low, medium, high
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")

#save model if the accuracy is better than 0.85
if accuracy > 0.85:
    model.save('costumer_clasifciation.h5')