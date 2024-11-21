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
healthy_path = "/Users/akankshborah/tjs_repo/tommy_john_surgery_modeling/.data/healthy/"
injured_path = "/Users/akankshborah/tjs_repo/tommy_john_surgery_modeling/.data/injured/"
healthy = {}
injured = {}
def valuegen_healthy(file):
    data = pd.read_csv(file)
    name = data['player_name']
    player_id = data.loc[0, 'pitcher']
    print(player_id)
    Fastballs = data.loc[data['pitch_type'].isin(['FF', 'SI'])]
    FF = data.loc[data['pitch_type'].isin(['FF'])]
    SI = data.loc[data['pitch_type'].isin(['SI'])]
    FC = data.loc[data['pitch_type'].isin(['FC'])]
    OFF = data.loc[~data['pitch_type'].isin(['FF', 'SI'])]
    CH = data.loc[data['pitch_type'].isin(['CH'])]
    SPL = data.loc[data['pitch_type'].isin(['FS', 'FO'])]
    SL = data.loc[data['pitch_type'].isin(['SL', 'SV', 'ST'])]
    Sweep = data.loc[data['pitch_type'].isin(['ST'])]
    CU = data.loc[data['pitch_type'].isin(['CU', 'KC', 'CS'])]
    mean_veloFF = FF['release_speed'].mean()
    mean_veloOFF = OFF['release_spin_rate'].mean()
    mean_release = data['release_pos_z'].mean()
    mean_spinFF = FF['release_spin_rate'].mean()
    mean_spinOFF = OFF['release_spin_rate'].mean()
    healthy[player_id] = [name, data, mean_veloFF, mean_veloOFF, mean_release, mean_spinFF, mean_spinOFF, Fastballs, FF, SI, FC, CH, SPL, SL, Sweep, CU, OFF]
    return data, mean_veloFF, mean_veloOFF, mean_release, mean_spinFF, mean_spinOFF


for filename in os.listdir(healthy_path):
    f = os.path.join(healthy_path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        valuegen_healthy(healthy_path+filename)

def valuegen_healthy(file):
    data = pd.read_csv(file)
    name = data['player_name']
    player_id = data.loc[0, 'pitcher']
    Fastballs = data.loc[data['pitch_type'].isin(['FF', 'SI'])]
    FF = data.loc[data['pitch_type'].isin(['FF'])]
    SI = data.loc[data['pitch_type'].isin(['SI'])]
    FC = data.loc[data['pitch_type'].isin(['FC'])]
    OFF = data.loc[~data['pitch_type'].isin(['FF', 'SI'])]
    CH = data.loc[data['pitch_type'].isin(['CH'])]
    SPL = data.loc[data['pitch_type'].isin(['FS', 'FO'])]
    SL = data.loc[data['pitch_type'].isin(['SL', 'SV', 'ST'])]
    Sweep = data.loc[data['pitch_type'].isin(['ST'])]
    CU = data.loc[data['pitch_type'].isin(['CU', 'KC', 'CS'])]
    mean_veloFF = FF['release_speed'].mean()
    mean_veloOFF = OFF['release_spin_rate'].mean()
    mean_release = data['release_pos_z'].mean()
    mean_spinFF = FF['release_spin_rate'].mean()
    mean_spinOFF = OFF['release_spin_rate'].mean()
    injured[player_id] = [name, data, mean_veloFF, mean_veloOFF, mean_release, mean_spinFF, mean_spinOFF, Fastballs, FF, SI, FC, CH, SPL, SL, Sweep, CU, OFF]
    return data, mean_veloFF, mean_veloOFF, mean_release, mean_spinFF, mean_spinOFF

for filename in os.listdir(injured_path):
    f = os.path.join(injured_path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        valuegen_healthy(injured_path+filename)

print(len(healthy))

print(len(injured))


