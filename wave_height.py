from netCDF4 import Dataset
import numpy as np
import math


fh = Dataset("cropped_wave2.nc", "r", format="NETCDF4")

lons = fh.variables['longitude'][:]
lats = fh.variables['latitude'][:]
tmax = fh.variables['time'][:]
tmax_units = fh.variables['time'].units

awh = fh.variables['awh'][:]
for a in awh:
    for b in a:
        for c in b:
            if c != "---":
                print(c)