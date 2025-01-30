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

healthy_path = "./.data/healthy/"
injured_path = "./.data/injured/"

healthy_data = []
injured_data = []


def valuegen_healthy(file):
    data = pd.read_csv(file)
    # data = data.drop(data[data['release_speed'] == None or data['release_pos_z'] == None].index)
    columns_to_check = ['release_extension', 'release_speed', 'release_pos_x', 'release_pos_z', 'release_pos_y', 'spin_axis', 'pitcher_days_since_prev_game', 'release_spin_rate', 'arm_angle']  # Replace with your column names
    data_cleaned = data.dropna(subset=columns_to_check)
    data_cleaned['TJ'] = 0
    injured_data.append(data_cleaned)
    return data_cleaned.head()

for filename in os.listdir(healthy_path):
    f = os.path.join(healthy_path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        valuegen_healthy(healthy_path+filename)


def valuegen_injured(file):
    data = pd.read_csv(file)
    # data = data.drop(data[data['release_speed'] == None or data['release_pos_z'] == None].index)
    columns_to_check = ['release_extension', 'release_speed', 'release_pos_x', 'release_pos_z', 'release_pos_y', 'spin_axis', 'pitcher_days_since_prev_game', 'release_spin_rate', 'arm_angle']  # Replace with your column names
    data_cleaned = data.dropna(subset=columns_to_check)
    data_cleaned['TJ'] = 1
    injured_data.append(data_cleaned)
    return data_cleaned.head()

for filename in os.listdir(injured_path):
    f = os.path.join(injured_path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        valuegen_injured(injured_path+filename)


combined_data = injured_data + healthy_data

combined_df = pd.concat(combined_data)

combined_df.to_csv(".data/all_filtered_data.csv", index=False)

print("Data combined successfully!")