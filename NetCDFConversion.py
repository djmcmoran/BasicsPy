import netCDF4
import pandas as pd

temp_nc_file = 'file_path'
nc = netCDF4.Dataset(temp_nc_file, mode='r')

nc.variables.keys()

lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
time_var = nc.variables['time']
dtime = netCDF4.num2date(time_var[:],time_var.units)
temp = nc.variables['precip'][:]

# a pandas.Series designed for time series of a 2D lat,lon grid
temp_ts = pd.Series(temp, index=dtime) 

temp_ts.to_csv('precip.csv',index=True, header=True)
