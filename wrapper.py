from Process import Process
import wind_speed as ws
import numpy as np

speed, density, cp, time, lons, lats = ws.get_wind_data()

p = Process()
a = p.dataProcess(speed,density,cp)

#print(a.shape)

print(np.sum(a,axis = 0).shape)
