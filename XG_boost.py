import pandas as pd
import numpy as np
import joblib

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix

import matplotlib.pyplot as plt
from xgboost import plot_importance


data = pd.read_csv("./.data/all_filtered_data.csv")


print(data.head())

# Define features and target
X = data[['release_extension', 'release_speed', 'release_pos_x', 'release_pos_z', 'release_pos_y', 'spin_axis', 'pitcher_days_since_prev_game', 'release_spin_rate', 'arm_angle']]
y = data['TJ']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# Initialize the XGBoost classifier
xgb_model = XGBClassifier(
    n_estimators=100,       # Number of boosting rounds
    max_depth=20,            # Maximum depth of each tree
    learning_rate=0.8,      # Step size shrinkage
    subsample=0.8,          # Subsampling ratio of the training instance
    colsample_bytree=0.8,   # Subsampling ratio of columns when constructing each tree
    random_state=42
)

# Train the model
xgb_model.fit(X_train, y_train)

# Predict on the test set
y_pred = xgb_model.predict(X_test)
y_pred_proba = xgb_model.predict_proba(X_test)[:, 1]  # For AUC-ROC

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))



# Plot feature importance
plot_importance(xgb_model)
plt.show()

# Save the model
joblib.dump(xgb_model, './.data/xg_boost_tj_risk_model_v1.pkl')
