from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
from pybaseball import statcast_pitcher_spin
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from pybaseball import player_search_list
import random
import os
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


healthy_path = "./.data/healthy/"
injured_path = "./.data/injured/"

healthy_data = []
injured_data = []


def valuegen_healthy(file):
    data = pd.read_csv(file)
    TJ_Values = []
    for i in data.values:
        TJ_Values.append(False)
    new_data = data.assign(TJ = TJ_Values)
    healthy_data.append(new_data)
    return new_data.head()

for filename in os.listdir(healthy_path):
    f = os.path.join(healthy_path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        valuegen_healthy(healthy_path+filename)


def valuegen_injured(file):
    data = pd.read_csv(file)
    TJ_Values = []
    for i in data.values:
        TJ_Values.append(True)
    new_data = data.assign(TJ = TJ_Values)
    injured_data.append(new_data)
    return new_data.head()

for filename in os.listdir(injured_path):
    f = os.path.join(injured_path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        valuegen_injured(injured_path+filename)


combined_data = injured_data + healthy_data

combined_df = pd.concat(combined_data)

print(combined_df.head())

X = combined_df[['release_speed', 'release_pos_z']]
y = combined_df['TJ']

scaler = StandardScaler()
X = scaler.fit_transform(X)  # Standardize features

# Initialize PCA and fit to data
pca = PCA(n_components=5)  # Choose 5 components (you can adjust this)
X_pca = pca.fit_transform(X)

# Check explained variance ratio
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Cumulative Explained Variance:", np.cumsum(pca.explained_variance_ratio_))

# Optional: Scree plot to decide number of components
plt.figure(figsize=(8, 6))
plt.plot(np.cumsum(pca.explained_variance_ratio_), marker='o')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Scree Plot')
plt.show()

# Initialize and fit the regression model
model = LinearRegression()
model.fit(X_pca, y)

# Check the model's performance
y_pred = model.predict(X_pca)
print("R-squared Score:", r2_score(y, y_pred))

# View the regression coefficients for each principal component
print("Regression Coefficients:", model.coef_)
