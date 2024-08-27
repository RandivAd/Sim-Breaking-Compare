import pandas as pd
import matplotlib.pyplot as plt

# Read in csv files and skip the first 14 lines as well as the line with units
rows_to_skip = list(range(0, 14))
data = pd.read_csv('nurburgring-lamborghini_huracan_gt3_evo-2.csv', on_bad_lines='skip', low_memory=False, skiprows= rows_to_skip)
data = data.drop(data.index[0])

hot_lap_data = pd.read_csv('nurburgring-mclaren_720s_gt3_evo.csv', on_bad_lines='skip', low_memory=False, skiprows= rows_to_skip)
hot_lap_data = hot_lap_data.drop(data.index[0])

# Turn csv values to numbers for it to be compared later
data['Time'] = pd.to_numeric(data['Time'], errors='coerce')
data['SPEED'] = pd.to_numeric(data['SPEED'], errors='coerce')
data['STEERANGLE'] = pd.to_numeric(data['STEERANGLE'], errors='coerce')
data['BRAKE'] = pd.to_numeric(data['BRAKE'], errors='coerce')

hot_lap_data['Time'] = pd.to_numeric(hot_lap_data['Time'], errors='coerce')
hot_lap_data['SPEED'] = pd.to_numeric(hot_lap_data['SPEED'], errors='coerce')
hot_lap_data['STEERANGLE'] = pd.to_numeric(hot_lap_data['STEERANGLE'], errors='coerce')
hot_lap_data['BRAKE'] = pd.to_numeric(hot_lap_data['BRAKE'], errors='coerce')

plt.figure(figsize=(14, 7))

# Plot Brake% over Time
plt.plot(data['Time'], data['BRAKE'], label='Brake% - Your Lap', color='blue')
plt.plot(hot_lap_data['Time'], hot_lap_data['BRAKE'], label='Break% - Hot Lap', color='red')
plt.xlabel('Time')
plt.ylabel('Brake%')
plt.title('Braking Points Over Time')
plt.legend()
plt.show()

# Look for braking points before turns
turns = data[(data['STEERANGLE'].abs() > 5) & (data['SPEED'] < 100)]
braking_before_turns = turns[turns['BRAKE'] > 50]
print("Braking before turns:")
print(braking_before_turns[['Time', 'SPEED', 'BRAKE', 'STEERANGLE']])