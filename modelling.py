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

print(combined_data.head())