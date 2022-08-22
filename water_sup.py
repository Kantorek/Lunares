import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

time = 20
tank_vol = 2000
usage_of_water = [1966, 1863, 1831, 1714, 1678]
dict = {'usage_of_water': usage_of_water}
df = pd.DataFrame(dict)
df.to_csv('data.csv')

#TODO: Implement adding data

# interpolating data 
usage_of_water = df['usage_of_water'].tolist()
days = []
for x in range(1, time*2+2):
  days.append(x)
time = len(usage_of_water)
days = np.arange(0, time, 1)
poly = np.polyfit(days, usage_of_water, deg=1)
p = np.poly1d(poly)
i = 0

for l in usage_of_water:
  if l > 0:
    plt.plot(i, l, 'r+')
    i += 1

# ploting the data
plt.plot(i-1, usage_of_water[-1], 'r+', label="Real usage of water")
days = np.arange(0, 2*time, 1)
days_left = int((np.roots(p)[0] - len(usage_of_water) + 1)/2)
plt.plot(days, p(days), label="Interpolated usage of water")
plt.xlim(0, len(days))
plt.ylim(0, tank_vol)
plt.title("Interpolation of water consumpion. {} days to end of water".format(days_left))
plt.xlabel("Days")
plt.ylabel("Water in tank [l]")
plt.legend()
plt.show()
