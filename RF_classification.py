import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt


data = pd.read_csv("./.data/all_filtered_data.csv")

# Define features and target
X = data[['release_extension', 'release_speed', 'release_pos_x', 'release_pos_z', 'release_pos_y', 'spin_axis', 'pitcher_days_since_prev_game', 'release_spin_rate', 'arm_angle']]
y = data['TJ']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Initialize the model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

importances = rf_model.feature_importances_

# Create a DataFrame for better visualization
importance_df = pd.DataFrame({
    'Feature': ['release_extension', 'release_speed', 'release_pos_x', 'release_pos_z', 'release_pos_y', 'spin_axis', 'pitcher_days_since_prev_game', 'release_spin_rate', 'arm_angle'],
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

# Plot feature importances
plt.figure(figsize=(8, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'], color='skyblue')
plt.gca().invert_yaxis()  # Highest importance on top
plt.xlabel('Feature Importance')
plt.ylabel('Feature')
plt.title('Random Forest Feature Importance')
plt.show()

# Save the model to a file
joblib.dump(rf_model, './.data/tommy_john_risk_model_v1.pkl')

# Load the model (for future use)
loaded_model = joblib.load('./.data/tommy_john_risk_model_v1.pkl')
