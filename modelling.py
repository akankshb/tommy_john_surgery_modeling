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
from sklearn.metrics import r2_score
from sklearn.manifold import TSNE


healthy_path = "./.data/healthy/"
injured_path = "./.data/injured/"

healthy_data = []
injured_data = []


def valuegen_healthy(file):
    data = pd.read_csv(file)
    TJ_Values = []
    columns_to_check = ['release_speed', 'release_pos_z', 'release_spin_rate', 'release_pos_x', 'release_extension', 'spin_axis', 'pitcher_days_since_prev_game']  # Replace with your column names
    data_cleaned = data.dropna(subset=columns_to_check)
    # data = data.drop(data[(data['release_speed'] == None) or (data['release_pos_z'] == None)].index)
    for i in data_cleaned.values:
        TJ_Values.append(False)
    new_data = data_cleaned.assign(TJ = TJ_Values)
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
    # data = data.drop(data[data['release_speed'] == None or data['release_pos_z'] == None].index)
    columns_to_check = ['release_speed', 'release_pos_z', 'release_spin_rate', 'release_pos_x', 'release_extension', 'spin_axis', 'pitcher_days_since_prev_game']  # Replace with your column names
    data_cleaned = data.dropna(subset=columns_to_check)
    for i in data_cleaned.values:
        TJ_Values.append(True)
    new_data = data_cleaned.assign(TJ = TJ_Values)
    injured_data.append(new_data)
    return new_data.head()

for filename in os.listdir(injured_path):
    f = os.path.join(injured_path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        valuegen_injured(injured_path+filename)


combined_data = injured_data + healthy_data

combined_df = pd.concat(combined_data)

# print(combined_df.head())

X = combined_df[['release_speed', 'release_pos_z', 'release_spin_rate', 'release_pos_x', 'release_extension', 'spin_axis', 'pitcher_days_since_prev_game']]
y = combined_df['TJ']

scaler = StandardScaler()
X = scaler.fit_transform(X)  # Standardize features

# Initialize PCA and fit to data
pca = PCA(n_components=7)  # Choose 5 components (you can adjust this)
X_pca = pca.fit_transform(X)

# Check explained variance ratio
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Cumulative Explained Variance:", np.cumsum(pca.explained_variance_ratio_))

# plt.figure(figsize=(8, 6))
# plt.plot(np.cumsum(pca.explained_variance_ratio_), marker='o')
# plt.xlabel('Number of Components')
# plt.ylabel('Cumulative Explained Variance')
# plt.title('Scree Plot')
# plt.show()

# Initialize and fit the regression model
model = LinearRegression()
model.fit(X_pca, y)

# Check the model's performance
y_pred = model.predict(X_pca)
print("R-squared Score:", r2_score(y, y_pred))

# the regression coefficients for each principal component
print("Regression Coefficients:", model.coef_)

# Finding the important features
loadings = pca.components_
print("Loadings:\n", loadings)

feature_importance = np.abs(loadings).sum(axis=0)
print("Overall Feature Importance:", feature_importance)

# Accessing all the numerical data points we need
TSNE_dataset = combined_df[['release_speed', 'release_pos_z', 'release_spin_rate', 'release_pos_x', 'release_extension', 'spin_axis', 'pitcher_days_since_prev_game']]
# Running the t-SNE
tsne = TSNE(learning_rate = 100) # Adjust learning rate
# Transform the features
tsne_features = tsne.fit_transform(TSNE_dataset)

# Assign to 2D array
tsne_features[1:4,:]

combined_df['x'] = tsne_features[:,0]

combined_df['y'] = tsne_features[:,1]


#Creating t-SNE scatterplot
plt.plot()

sns.scatterplot(x='x', y= 'y', hue= 'TJ', data = combined_df, alpha = 0.5)

plt.show()