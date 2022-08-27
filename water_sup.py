import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

time = 20
tank_vol = 2000

usage_of_water = []
dict = {'usage_of_water': usage_of_water}
df = pd.DataFrame(dict)

print('Welcome in WaterExp 1.0: ')
while True:
  todo_str = input('Import data from csv file (i), add new data (a), delete data (d), calculate interpolation (c): ')
  if todo_str == 'i':
    df = pd.read_csv('data.csv')
    print(df)
  elif todo_str == 'a':
    new_data = input('Entry new data: ')
    try:
      new_data = int(new_data)
    except:
      print('Wrong type of data')
      continue
    df.loc[len(df.index)] = new_data
    print(df)
    df.to_csv('data.csv')
    continue
  elif todo_str == 'd':
    empty_df = pd.DataFrame({'usage_of_water': []})
    empty_df.to_csv('data.csv')
    continue
  elif todo_str == 'c':
    break
  else:
    print('Wrong commend, type the correct one')
    continue
  break

# interpolating data 
# TODO: Looping for the best interpolation deg and roots
usage_of_water = df['usage_of_water'].tolist()
days = []
for x in range(1, time*2+2):
  days.append(x)
time = len(usage_of_water)
days = np.arange(0, time, 1)
poly = np.polyfit(days, usage_of_water, deg=1)
p = np.poly1d(poly)

days = np.arange(0, 2*time, 1)
days_left = int((np.roots(p)[0] - len(usage_of_water) + 1)/2)
# ploting real data
i = 0
for l in usage_of_water:
  if l > 0:
    plt.plot(i, l, 'r+')
    i += 1
plt.plot(i-1, usage_of_water[-1], 'r+', label="Real usage of water")

# ploting interpolated data
plt.plot(days, p(days), label="Interpolated usage of water")

plt.xlim(0, len(days))
plt.ylim(0, tank_vol)

plt.title("Interpolation of water consumpion. {} days to end of water".format(days_left))
plt.xlabel("Days")
plt.ylabel("Water in tank [l]")
plt.legend()
plt.show()
