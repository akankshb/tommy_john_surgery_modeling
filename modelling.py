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
healthy = {}
injured = {}
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


healthy_Fastball_data = []
for key in healthy.keys():
  x = healthy[key][7]
  y = []
  for i in x.values:
    y.append(0)
  z = x.assign(TJ = y)
  healthy_Fastball_data.append(z)
injured_Fastball_data = []
for key in injured.keys():
  x = injured[key][7]
  y = []
  for i in x.values:
    y.append(1)
  z = x.assign(TJ = y)
  injured_Fastball_data.append(z)
# for key in unhealthy.keys():
#   x = unhealthy[key][8]
#   Fastball_data.append(x)
Healthy_df = pd.concat(healthy_Fastball_data)
Injured_df = pd.concat(injured_Fastball_data)

plt.plot()
Injured_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Velocity', density = True)
Healthy_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Velocity', density = True)
plt.xlabel("Velocity")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Release Height', density = True)
Healthy_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Release Height', density = True)
plt.xlabel("Release Height")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Spin Rate', density = True)
Healthy_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers Spin Rate', density = True)
plt.xlabel("Spin Rate")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_df['release_extension'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Extension', density = True)
Healthy_df['release_extension'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers Extension', density = True)
plt.xlabel("Extension")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Fastball Spin Axis', density = True)
Healthy_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Regular Pitchers Fastball Spin Axis', density = True)
plt.xlabel("Axis")
plt.ylabel("Frequency")
plt.legend()
plt.show()



healthy_FF_data = []
for key in healthy.keys():
  x = healthy[key][8]
  y = []
  for i in x.values:
    y.append(0)
  z = x.assign(TJ = y)
  healthy_FF_data.append(z)

injured_FF_data = []
for key in injured.keys():
  x = injured[key][8]
  y = []
  for i in x.values:
    y.append(1)
  z = x.assign(TJ = y)
  injured_FF_data.append(z)
Healthy_FF_df = pd.concat(healthy_FF_data)
Injured_FF_df = pd.concat(injured_FF_data)

plt.plot()
Injured_FF_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher FF Velocity', color = 'Green', density = True)
Healthy_FF_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers FF Velocity', color = 'Red', density = True)
plt.xlabel("Velocity")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_FF_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher FF Release Height', color = 'Green', density = True)
Healthy_FF_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers FF Release Height', color = 'Red', density = True)
plt.xlabel("Release Height")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_FF_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher FF Spin Rate', color = 'Green', density = True)
Healthy_FF_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers FF Spin Rate', color = 'Red', density = True)
plt.xlabel("Spin Rate")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_FF_df['release_extension'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher FF Extension', color = 'Green', density = True)
Healthy_FF_df['release_extension'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers FF Extension', color = 'Red', density = True)
plt.xlabel("Extension")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_FF_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher FF Spin Axis', color = 'Green', density = True)
Healthy_FF_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Regular Pitchers FF Spin Axis', color = 'Red', density = True)
plt.xlabel("Axis")
plt.ylabel("Frequency")
plt.legend()
plt.show()

healthy_SI_data = []
for key in healthy.keys():
  x = healthy[key][9]
  y = []
  for i in x.values:
    y.append(0)
  z = x.assign(TJ = y)
  healthy_SI_data.append(z)
injured_SI_data = []
for key in injured.keys():
  x = injured[key][9]
  y = []
  for i in x.values:
    y.append(1)
  z = x.assign(TJ = y)
  injured_SI_data.append(z)

Healthy_SI_df = pd.concat(healthy_SI_data)
Injured_SI_df = pd.concat(injured_SI_data)

plt.plot()
Injured_SI_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Sinker Velocity', density = True)
Healthy_SI_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Sinker Velocity', density  = True)
plt.xlabel("Velocity")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SI_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Sinker Release Height', density = True)
Healthy_SI_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Sinker Release Height', density = True)
plt.xlabel("Release Height")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SI_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Sinker Spin Rate', density = True)
Healthy_SI_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers Sinker Spin Rate', density = True)
plt.xlabel("Spin Rate")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SI_df['release_extension'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Sinker Extension', density = True)
Healthy_SI_df['release_extension'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers Sinker Extension', density = True)
plt.xlabel("Extension")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SI_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Sinker Spin Axis', density = True)
Healthy_SI_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Regular Pitchers Sinker Spin Axis', density = True)
plt.xlabel("Axis")
plt.ylabel("Frequency")
plt.legend()
plt.show()

healthy_FC_data = []
for key in healthy.keys():
  x = healthy[key][10]
  y = []
  for i in x.values:
    y.append(0)
  z = x.assign(TJ = y)
  healthy_FC_data.append(z)
injured_FC_data = []
for key in injured.keys():
  x = injured[key][10]
  y = []
  for i in x.values:
    y.append(1)
  z = x.assign(TJ = y)
  injured_FC_data.append(z)

Healthy_FC_df = pd.concat(healthy_FC_data)
Injured_FC_df = pd.concat(injured_FC_data)

plt.plot()
Injured_FC_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher FC Velocity', color = 'Green', density = True)
Healthy_FC_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers FC Velocity', color = 'Red', density = True)
plt.xlabel("Velocity")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_FC_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher FC Release Height', color = 'Green', density  = True)
Healthy_FC_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers FC Release Height', color = 'Red', density = True)
plt.xlabel("Release Height")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_FC_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher FC Spin Rate', color = 'Green', density = True)
Healthy_FC_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers FC Spin Rate', color = 'Red', density = True)
plt.xlabel("Spin Rate")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_FC_df['release_extension'].hist(bins = 20, alpha = 0.7, label = 'Tommy John Pitcher FC Extension', color = 'Green', density = True)
Healthy_FC_df['release_extension'].hist(bins = 20, alpha = 0.7, label = 'Regular Pitchers FC Extension', color = 'Red', density = True)
plt.xlabel("Extension")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_FC_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher FC Spin Axis', color = 'Green', density = True)
Healthy_FC_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Regular Pitchers FC Spin Axis', color = 'Red', density = True)
plt.xlabel("Axis")
plt.ylabel("Frequency")
plt.legend()
plt.show()

