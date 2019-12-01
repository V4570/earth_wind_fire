from Process import Process
import DogasParser as lilg # little george dogas
import wind_speed as ws
import numpy as np

def get_monthly():
    import ipdb;ipdb.set_trace()

    speed, density, cp, time, lons, lats = ws.get_wind_data()

    p = Process()

    energyPerMonth = p.dataProcess(speed,density,cp)

    mask = lilg.get_data()

    maskedEnergyPerMonth = p.applyMaks(energyPerMonth, mask)
    return (maskedEnergyPerMonth, lats, lons, np.max(energyPerMonth))

# vz.vizualize(energyPerMonth, lons, lats)


get_monthly()