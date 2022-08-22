import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

time = 20

tank_vol = 2000
usage_of_water = []
days = []
for x in range(1, time*2+2):
  days.append(x)

for l in [1966, 1863, 1831, 1714, 1678, 1577, 1494, 1380, 1256, 1217, 1180, 1139, 1034, 925, 869, 773, 732, 682]:
  usage_of_water.append(l)
time = len(usage_of_water)
days = np.arange(0, time, 1)
poly = np.polyfit(days, usage_of_water, deg=4)
p = np.poly1d(poly)
i = 0
for l in usage_of_water:
  if l > 0:
    plt.plot(i, l, 'r+')
    i += 1
plt.plot(i-1, usage_of_water[-1], 'r+', label="Real usage of water")
days = np.arange(0, 2*time, 1)
days_left = int((np.roots(p)[3] - len(usage_of_water) + 1)/2)
plt.plot(days, p(days), label="Interpolated usage of water")
plt.xlim(0, len(days))
plt.ylim(0, tank_vol)
plt.title("Interpolation of water consumpion. {} days to end of water".format(days_left))
plt.xlabel("Days")
plt.ylabel("Water in tank [l]")
plt.legend()
plt.show()
