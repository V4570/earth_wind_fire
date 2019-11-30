from Process import Process
import wind_speed as ws
import numpy as np

speed, density, cp, time, lons, lats = ws.get_wind_data()

p = Process()
_, a = p.dataProcess(speed,density,cp)

print(a.shape)

#print(np.sum(a,axis = 3).shape)
