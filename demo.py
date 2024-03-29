from netCDF4 import Dataset
import numpy as np
import math

def find_density(t, mapping):
    min_diff = 9999
    tmp = 0
    for m in mapping:
        d = abs(t-m)
        if d < min_diff:
            tmp = m
            min_diff = d
    return mapping[tmp]



def get_wind_data():
    CP = 0.4

    mapping = {
    -40: 1.514,
    -35: 1.4843,
    -30: 1.395,
    -25: 1.4243,
    -10: 1.399,
    -5: 1.3178,
    0: 1.269,
    10: 1.247,
    15: 1.225,
    20: 1.204,
    25: 1.184,
    30: 1.165,
    40: 1.127,
    50: 1.109
    }

    fh = Dataset("cropped_dummy.nc", "r", format="NETCDF4")

    # latbounds = [35.01186, 41.50306]
    # lonbounds = [19.91975, 28.2225]

    lons = fh.variables['longitude'][:]
    lats = fh.variables['latitude'][:]

    tmax = fh.variables['time'][:]
    tmax_units = fh.variables['time'].units

    temp = fh.variables['t2m'][:] - 273.15

    u10 = fh.variables['u10'][:]
    v10 = fh.variables['v10'][:]

    np_u10 = np.array(u10)**2
    np_v10 = np.array(v10)**2

    speed = np.sqrt(np.add(np_u10, np_v10))

    nullified_speed = np.where([(speed > 3) & (speed < 25)], speed, 0)

    vec_func = np.vectorize(find_density)
    c = np.array(temp)

    density = np.array(vec_func(c, mapping))

    efficiency = 0.5 * CP * np.multiply(density, np.power(nullified_speed,3))[0]
    
    return (efficiency[0], lats, lons, np.max(efficiency[0]))

if __name__ == '__main__':
    get_wind_data()
