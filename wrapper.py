from Process import Process
import wind_speed as ws
import numpy as np

def get_monthly():
    speed, density, cp, time, lons, lats = ws.get_wind_data()

    p = Process()

    energyPerMonth = p.dataProcess(speed,density,cp)

    return (energyPerMonth, lats, lons, np.max(energyPerMonth))

# vz.vizualize(energyPerMonth, lons, lats)