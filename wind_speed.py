from netCDF4 import Dataset
import numpy as np
import math


fh = Dataset("cropped_wind.nc", "r", format="NETCDF4")

# latbounds = [35.01186, 41.50306]
# lonbounds = [19.91975, 28.2225]

lons = fh.variables['longitude'][:]
lats = fh.variables['latitude'][:]

# latli = np.argmin(np.abs(lats - latbounds[0]))
# latui = np.argmin(np.abs(lats - latbounds[1]))

# lonli = np.argmin(np.abs(lons - lonbounds[0]))
# lonui = np.argmin(np.abs(lons - lonbounds[1]))

# print(latli,latui, lonli,lonui)

tmax = fh.variables['time'][:]

tmax_units = fh.variables['time'].units

# awh = fh.variables['awh'][:]
# print(rootgrp.get_variables_by_attributes(standard_name='altimeter_wave_height'))

temp = fh.variables['t2m'][:] - 273.15
pressure = fh.variables['sp'][:]

u10 = fh.variables['u10'][:]
v10 = fh.variables['v10'][:]

np_u10 = np.array(u10)**2
np_v10 = np.array(v10)**2

speed = np.sqrt(np.add(np_u10, np_v10))

print(temp)