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

print("Amount of Cutters Thrown by Healthy Pitchers: " + str(Healthy_FC_df.shape))
print("Amount of Cutters Thrown by Tommy John Pitchers: "+ str(Injured_FC_df.shape))

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


healthy_CH_data = []
for key in healthy.keys():
  x = healthy[key][11]
  y = []
  for i in x.values:
    y.append(0)
  z = x.assign(TJ = y)
  healthy_CH_data.append(z)
injured_CH_data = []
for key in injured.keys():
  x = injured[key][11]
  y = []
  for i in x.values:
    y.append(1)
  z = x.assign(TJ = y)
  injured_CH_data.append(z)

Healthy_CH_df = pd.concat(healthy_CH_data)
Injured_CH_df = pd.concat(injured_CH_data)

print("Amount of Changeups Thrown by Healthy Pitchers: " + str(Healthy_CH_df.shape))
print("Amount of Changeups Thrown by Tommy John Pitchers: "+ str(Injured_CH_df.shape))

plt.plot()
Injured_CH_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Changeup Velocity', color = 'slateblue', density = True)
Healthy_CH_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Changeup Velocity', color = 'crimson', density = True)
plt.xlabel("Velocity")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_CH_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Changeup Release Height', color = 'slateblue', density = True)
Healthy_CH_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Changeup Release Height', color = 'crimson', density = True)
plt.xlabel("Release Height")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_CH_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Changeup Spin Rate', color = 'slateblue', density = True)
Healthy_CH_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers Changeup Spin Rate', color = 'crimson', density = True)
plt.xlabel("Spin Rate")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_CH_df['release_extension'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Changeup Extension', color = 'slateblue', density = True)
Healthy_CH_df['release_extension'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers Changeup Extension', color = 'crimson', density = True)
plt.xlabel("Extension")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_CH_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Changeup Spin Axis', color = 'slateblue', density = True)
Healthy_CH_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Regular Pitchers Changeup Spin Axis', color = 'crimson', density = True)
plt.xlabel("Axis")
plt.ylabel("Frequency")
plt.legend()
plt.show()

healthy_SPL_data = []
for key in healthy.keys():
  x = healthy[key][12]
  y = []
  for i in x.values:
    y.append(0)
  z = x.assign(TJ = y)
  healthy_SPL_data.append(z)
injured_SPL_data = []
for key in injured.keys():
  x = injured[key][12]
  y = []
  for i in x.values:
    y.append(1)
  z = x.assign(TJ = y)
  injured_SPL_data.append(z)

Healthy_SPL_df = pd.concat(healthy_SPL_data)
Injured_SPL_df = pd.concat(injured_SPL_data)

print("Amount of Splitters Thrown by Healthy Pitchers: " + str(Healthy_SPL_df.shape))
print("Amount of Splitters Thrown by Tommy John Pitchers: "+ str(Injured_SPL_df.shape))

plt.plot()
Injured_SPL_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Splitter Velocity', density = True)
Healthy_SPL_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Splitter Velocity', density = True)
plt.xlabel("Velocity")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SPL_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Splitter Release Height', density = True)
Healthy_SPL_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Splitter Release Height', density = True)
plt.xlabel("Release Height")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SPL_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Splitter Spin Rate', density = True)
Healthy_SPL_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers Splitter Spin Rate', density = True)
plt.xlabel("Spin Rate")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SPL_df['release_extension'].hist(bins = 20, alpha = 0.7, label = 'Tommy John Pitcher Splitter Extension', density = True)
Healthy_SPL_df['release_extension'].hist(bins = 20, alpha = 0.7, label = 'Regular Pitchers Splitter Extension', density = True)
plt.xlabel("Extension")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SPL_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Splitter Spin Axis', density = True)
Healthy_SPL_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Regular Pitchers Splitter Spin Axis', density = True)
plt.xlabel("Axis")
plt.ylabel("Frequency")
plt.legend()
plt.show()

healthy_slider_data = []
for key in healthy.keys():
  x = healthy[key][13]
  y = []
  for i in x.values:
    y.append(0)
  z = x.assign(TJ = y)
  healthy_slider_data.append(z)

injured_slider_data = []
for key in injured.keys():
  x = injured[key][13]
  y = []
  for i in x.values:
    y.append(1)
  z = x.assign(TJ = y)
  injured_slider_data.append(z)
Healthy_slider_df = pd.concat(healthy_slider_data)
Injured_slider_df = pd.concat(injured_slider_data)

print("Amount of Sliders Thrown by Healthy Pitchers: " + str(Healthy_slider_df.shape))
print("Amount of Sliders Thrown by Tommy John Pitchers: "+ str(Injured_slider_df.shape))

plt.plot()
Injured_slider_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Slider Velocity', color = 'slateblue', density = True)
Healthy_slider_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Slider Velocity', color = 'crimson', density = True)
plt.xlabel("Velocity")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_slider_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Slider Release Height', color = 'slateblue', density = True)
Healthy_slider_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Slider Release Height', color = 'crimson', density = True)
plt.xlabel("Release Height")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_slider_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Slider Spin Rate', color = 'slateblue', density = True)
Healthy_slider_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers Slider Spin Rate', color = 'crimson', density = True)
plt.xlabel("Spin Rate")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_slider_df['release_extension'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Slider Extension', color = 'slateblue', density = True)
Healthy_slider_df['release_extension'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers Slider Extension', color = 'crimson', density = True)
plt.xlabel("Extension")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_slider_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Slider Spin Axis', color = 'slateblue', density  = True)
Healthy_slider_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Regular Pitchers Slider Spin Axis', color = 'crimson', density = True)
plt.xlabel("Axis")
plt.ylabel("Frequency")
plt.legend()
plt.show()

healthy_SWP_data = []
for key in healthy.keys():
  x = healthy[key][14]
  y = []
  for i in x.values:
    y.append(0)
  z = x.assign(TJ = y)
  healthy_SWP_data.append(z)
injured_SWP_data = []
for key in injured.keys():
  x = injured[key][14]
  y = []
  for i in x.values:
    y.append(1)
  z = x.assign(TJ = y)
  injured_SWP_data.append(z)

Healthy_SWP_df = pd.concat(healthy_SWP_data)
Injured_SWP_df = pd.concat(injured_SWP_data)

print("Amount of Sweepers Thrown by Healthy Pitchers: " + str(Healthy_SWP_df.shape))
print("Amount of Sweepers Thrown by Tommy John Pitchers: "+ str(Injured_SWP_df.shape))

plt.plot()
Injured_SWP_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher SWP Velocity', color = 'Green', density = True)
Healthy_SWP_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers SWP Velocity', color = 'Red', density = True)
plt.xlabel("Velocity")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SWP_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher SWP Release Height', color = 'Green', density = True)
Healthy_SWP_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers SWP Release Height', color = 'Red', density = True)
plt.xlabel("Release Height")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SWP_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher SWP Spin Rate', color = 'Green', density = True)
Healthy_SWP_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers SWP Spin Rate', color = 'Red', density = True)
plt.xlabel("Spin Rate")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SWP_df['release_extension'].hist(bins = 20, alpha = 0.7, label = 'Tommy John Pitcher SWP Extension', color = 'Green', density = True)
Healthy_SWP_df['release_extension'].hist(bins = 20, alpha = 0.7, label = 'Regular Pitchers SWP Extension', color = 'Red', density = True)
plt.xlabel("Extension")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_SWP_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher SWP Spin Axis', color = 'Green', density = True)
Healthy_SWP_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Regular Pitchers SWP Spin Axis', color = 'Red', density = True)
plt.xlabel("Axis")
plt.ylabel("Frequency")
plt.legend()
plt.show()

healthy_CU_data = []
for key in healthy.keys():
  x = healthy[key][15]
  y = []
  for i in x.values:
    y.append(0)
  z = x.assign(TJ = y)
  healthy_CU_data.append(z)
injured_CU_data = []
for key in injured.keys():
  x = injured[key][15]
  y = []
  for i in x.values:
    y.append(1)
  z = x.assign(TJ = y)
  injured_CU_data.append(z)

Healthy_CU_df = pd.concat(healthy_CU_data)
Injured_CU_df = pd.concat(injured_CU_data)

print("Amount of Curveballs Thrown by Healthy Pitchers: " + str(Healthy_CU_df.shape))
print("Amount of Curveballs Thrown by Tommy John Pitchers: "+ str(Injured_CU_df.shape))

plt.plot()
Injured_CU_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Curveball Velocity', color = 'slateblue', density = True)
Healthy_CU_df['release_speed'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Curveball Velocity', color = 'crimson', density = True)
plt.xlabel("Velocity")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_CU_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Tommy John Pitcher Curveball Release Height', color = 'slateblue', density = True)
Healthy_CU_df['release_pos_z'].hist(bins = 60, alpha = 0.7, label = 'Regular Pitchers Curveball Release Height', color = 'crimson', density = True)
plt.xlabel("Release Height")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_CU_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Curveball Spin Rate', color = 'slateblue', density = True)
Healthy_CU_df['release_spin_rate'].hist(bins = 40, alpha = 0.7, label = 'Regular Pitchers Curveball Spin Rate', color = 'crimson', density = True)
plt.xlabel("Spin Rate")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_CU_df['release_extension'].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Curveball Extension', color = 'slateblue', density = True)
Healthy_CU_df['release_extension'].hist(bins = 30, alpha = 0.7, label = 'Regular Pitchers Curveball Extension', color = 'crimson', density = True)
plt.xlabel("Extension")
plt.ylabel("Frequency")
plt.legend()
plt.show()
plt.plot()
Injured_CU_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Curveball Spin Axis', color = 'slateblue', density = True)
Healthy_CU_df['spin_axis'].hist(bins = 30, alpha = 0.7, label = 'Regular Pitchers Curveball Spin Axis', color = 'crimson', density = True)
plt.xlabel("Axis")
plt.ylabel("Frequency")
plt.legend()
plt.show()

healthy_fastball_percentages = []
for key in healthy.keys():
  x = len(healthy[key][1])
  y = len(healthy[key][7])
  try:
    percentage = y/x *100
  except:
    percentage = 0
  if percentage != 0:
    healthy_fastball_percentages.append(percentage)
injured_fastball_percentages = []
for key in injured.keys():
  x = len(injured[key][1])
  y = len(injured[key][7])
  try:
    percentage = y/x *100
  except ZeroDivisionError:
    percentage = 0
  if percentage != 0:
    injured_fastball_percentages.append(percentage)
Healthy_Fastball_percentage_df = pd.DataFrame(healthy_fastball_percentages)
Injured_Fastball_percentage_df = pd.DataFrame(injured_fastball_percentages)

plt.plot()
Healthy_Fastball_percentage_df[0].hist(bins = 30, alpha= 0.7, label = 'Healthy Pitcher Fastball Percentage', density = True)
Injured_Fastball_percentage_df[0].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Fastball Percentage', density = True)
plt.legend()
plt.show()

healthy_SL_percentages = []
for key in healthy.keys():
  x = len(healthy[key][1])
  y = len(healthy[key][13])
  try:
    percentage = y/x *100
  except:
    percentage = 0
  if percentage != 0:
    healthy_SL_percentages.append(percentage)
injured_SL_percentages = []
for key in injured.keys():
  x = len(injured[key][1])
  y = len(injured[key][13])
  try:
    percentage = y/x *100
  except ZeroDivisionError:
    percentage = 0
  if percentage != 0:
      injured_SL_percentages.append(percentage)
Healthy_SL_percentage_df = pd.DataFrame(healthy_SL_percentages)
Injured_SL_percentage_df = pd.DataFrame(injured_SL_percentages)

plt.plot()
Healthy_SL_percentage_df[0].hist(bins = 40, alpha= 0.7, label = 'Healthy Pitcher Slider Percentage', density = True)
Injured_SL_percentage_df[0].hist(bins = 40, alpha = 0.7, label = 'Tommy John Pitcher Slider Percentage', density = True)
plt.legend()
plt.show()

healthy_SWP_percentages = []
for key in healthy.keys():
  x = len(healthy[key][1])
  y = len(healthy[key][14])
  try:
    percentage = y/x *100
  except:
    percentage = 0
  if percentage != 0:
    healthy_SWP_percentages.append(percentage)
injured_SWP_percentages = []
for key in injured.keys():
  x = len(injured[key][1])
  y = len(injured[key][14])
  try:
    percentage = y/x *100
  except ZeroDivisionError:
    percentage = 0
  if percentage != 0:
      injured_SWP_percentages.append(percentage)
Healthy_SWP_percentage_df = pd.DataFrame(healthy_SWP_percentages)
Injured_SWP_percentage_df = pd.DataFrame(injured_SWP_percentages)

print("Amount of Healthy Pitchers that throw Sweepers: " + str(Healthy_SWP_percentage_df.shape))
print("Amount of Tommy John Pitchers that throw Sweepers: "+ str(Injured_SWP_percentage_df.shape))

plt.plot()
Healthy_SWP_percentage_df[0].hist(bins = 10, alpha= 0.7, label = 'Healthy Pitcher Sweeper Percentage', density = True)
Injured_SWP_percentage_df[0].hist(bins = 10, alpha = 0.7, label = 'Tommy John Pitcher Sweeper Percentage', density = True)
plt.legend()
plt.show()

healthy_SPL_percentages = []
for key in healthy.keys():
  x = len(healthy[key][1])
  y = len(healthy[key][14])
  try:
    percentage = y/x *100
  except:
    percentage = 0
  if percentage != 0:
    healthy_SPL_percentages.append(percentage)
injured_SPL_percentages = []
for key in injured.keys():
  x = len(injured[key][1])
  y = len(injured[key][14])
  try:
    percentage = y/x *100
  except ZeroDivisionError:
    percentage = 0
  if percentage != 0:
      injured_SPL_percentages.append(percentage)
Healthy_SPL_percentage_df = pd.DataFrame(healthy_SPL_percentages)
Injured_SPL_percentage_df = pd.DataFrame(injured_SPL_percentages)

print("Amount of Healthy Pitchers that throw Splitters: " + str(Healthy_SPL_percentage_df.shape))
print("Amount of Tommy John Pitchers that throw Splitters: "+ str(Injured_SPL_percentage_df.shape))

plt.plot()
Healthy_SPL_percentage_df[0].hist(bins = 10, alpha= 0.7, label = 'Healthy Pitcher Splitter Percentage', density = True)
Injured_SPL_percentage_df[0].hist(bins = 10, alpha = 0.7, label = 'Tommy John Pitcher Splitter Percentage', density = True)
plt.legend()
plt.show()

healthy_SI_percentages = []
for key in healthy.keys():
  x = len(healthy[key][1])
  y = len(healthy[key][9])
  try:
    percentage = y/x *100
  except:
    percentage = 0
  if percentage != 0:
    healthy_SI_percentages.append(percentage)
injured_SI_percentages = []
for key in injured.keys():
  x = len(injured[key][1])
  y = len(injured[key][9])
  try:
    percentage = y/x *100
  except ZeroDivisionError:
    percentage = 0
  if percentage != 0:
      injured_SI_percentages.append(percentage)
Healthy_SI_percentage_df = pd.DataFrame(healthy_SI_percentages)
Injured_SI_percentage_df = pd.DataFrame(injured_SI_percentages)

plt.plot()
Healthy_SI_percentage_df[0].hist(bins = 30, alpha= 0.7, label = 'Healthy Pitcher Sinker Percentage', density = True)
Injured_SI_percentage_df[0].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Sinker Percentage', density = True)
plt.legend()
plt.show()

healthy_CH_percentages = []
for key in healthy.keys():
  x = len(healthy[key][1])
  y = len(healthy[key][11])
  try:
    percentage = y/x *100
  except:
    percentage = 0
  if percentage != 0:
    healthy_CH_percentages.append(percentage)
injured_CH_percentages = []
for key in injured.keys():
  x = len(injured[key][1])
  y = len(injured[key][11])
  try:
    percentage = y/x *100
  except ZeroDivisionError:
    percentage = 0
  if percentage != 0:
      injured_CH_percentages.append(percentage)
Healthy_CH_percentage_df = pd.DataFrame(healthy_CH_percentages)
Injured_CH_percentage_df = pd.DataFrame(injured_CH_percentages)

print("Amount of Healthy Pitchers that throw Changeups: " + str(Healthy_CH_percentage_df.shape))
print("Amount of Tommy John Pitchers that throw Changeups: "+ str(Injured_CH_percentage_df.shape))

plt.plot()
Healthy_CH_percentage_df[0].hist(bins = 30, alpha= 0.7, label = 'Healthy Pitcher Changeup Percentage', density = True)
Injured_CH_percentage_df[0].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Changeup Percentage', density = True)
plt.legend()
plt.show()


healthy_CU_percentages = []
for key in healthy.keys():
  x = len(healthy[key][1])
  y = len(healthy[key][15])
  try:
    percentage = y/x *100
  except:
    percentage = 0
  if percentage != 0:
    healthy_CU_percentages.append(percentage)
injured_CU_percentages = []
for key in injured.keys():
  x = len(injured[key][1])
  y = len(injured[key][15])
  try:
    percentage = y/x *100
  except ZeroDivisionError:
    percentage = 0
  if percentage != 0:
      injured_CU_percentages.append(percentage)
Healthy_CU_percentage_df = pd.DataFrame(healthy_CU_percentages)
Injured_CU_percentage_df = pd.DataFrame(injured_CU_percentages)

print("Amount of Healthy Pitchers that throw Curveballs: " + str(Healthy_CU_percentage_df.shape))
print("Amount of Tommy John Pitchers that throw Curveballs: "+ str(Injured_CU_percentage_df.shape))


plt.plot()
Healthy_CU_percentage_df[0].hist(bins = 30, alpha= 0.7, label = 'Healthy Pitcher Curveball Percentage', density = True)
Injured_CU_percentage_df[0].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Curveball Percentage', density = True)
plt.legend()
plt.show()

healthy_FC_percentages = []
for key in healthy.keys():
  x = len(healthy[key][1])
  y = len(healthy[key][10])
  try:
    percentage = y/x *100
  except:
    percentage = 0
  if percentage != 0:
    healthy_FC_percentages.append(percentage)
injured_FC_percentages = []
for key in injured.keys():
  x = len(injured[key][1])
  y = len(injured[key][10])
  try:
    percentage = y/x *100
  except ZeroDivisionError:
    percentage = 0
  if percentage != 0:
      injured_FC_percentages.append(percentage)
Healthy_FC_percentage_df = pd.DataFrame(healthy_FC_percentages)
Injured_FC_percentage_df = pd.DataFrame(injured_FC_percentages)

print("Amount of Healthy Pitchers that throw Cutters: " + str(Healthy_FC_percentage_df.shape))
print("Amount of Tommy John Pitchers that throw Cutters: "+ str(Injured_FC_percentage_df.shape))


plt.plot()
Healthy_FC_percentage_df[0].hist(bins = 30, alpha= 0.7, label = 'Healthy Pitcher Cutter Percentage', density = True)
Injured_FC_percentage_df[0].hist(bins = 30, alpha = 0.7, label = 'Tommy John Pitcher Cutter Percentage', density = True)
plt.legend()
plt.show()


plt.plot()
for key in injured.keys():
  set = injured[key][8]
  sns.scatterplot(data = set, x = 'release_speed', y= 'release_pos_z', alpha = 0.75, c = 'Blue')
plt.title("Fastball Velocity vs Release Height Data for Tommy John")
plt.xlim(85, 120)
plt.show()