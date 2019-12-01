from Process import Process
import wind_speed as ws
import vizualize as vz
import numpy as np

speed, density, cp, time, lons, lats = ws.get_wind_data()

p = Process()

energyPerMonth = p.dataProcess(speed,density,cp)

vz.vizualize(energyPerMonth, lons, lats)

