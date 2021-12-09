# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:34:13 2021

@author: silva
"""

import numpy as np
from netCDF4 import Dataset
import pandas as pd


#TG#
data = Dataset(r'C:\Users\silva\Desktop\Carlo\9. Dati Pesanti\ECA&D\23.1\tg_ens_mean_0.25deg_reg_v23.1e.nc', 'r')

lat = data.variables['latitude']
lon = data.variables['longitude']
time = data.variables['time']
tg = data.variables['tg']

time_data=data.variables['time'][:]

lat_data=data.variables['latitude'][:]
lon_data=data.variables['longitude'][:]


cities=pd.read_excel('Cities.xlsx', sheet_name='LT', engine='openpyxl')


for index, row in cities.iterrows():
    print(row['Name'])




for index, row in cities.iterrows():
    location = (row['Name'])
    location_latitude = (row['Latitude'])
    location_longitude = (row['Longitude'])


    sq_diff_lat = (lat_data - location_latitude)**2
    sq_diff_lon = (lon_data - location_longitude)**2
    
    min_index_lat = sq_diff_lat.argmin()
    min_index_lon = sq_diff_lon.argmin()
    
    temp=data.variables['tg']
    
    
    
    
    data.variables['time']
    
    
    data.variables['time'].units[11:21]
    
    #Creating an empty pandas dataframe
    starting_date = data.variables['time'].units[11:21]
    ending_date = '2020-12-31'
    
    date_range = pd.date_range(start= starting_date, end=ending_date)
    df= pd.DataFrame(0,columns = ['tg'], index= date_range)
    
    
    data.variables['time'].size
    dt = np.arange(0, data.variables['time'].size)
    
    
    for time_index in dt: 
        df.iloc[time_index] = temp[time_index, min_index_lat,min_index_lon]
    
    
    
    df.to_csv(location +'.csv')

#TX#
data = Dataset(r'C:\Users\silva\Desktop\Carlo\9. Dati Pesanti\ECA&D\23.1\tx_ens_mean_0.25deg_reg_v23.1e.nc', 'r')

lat = data.variables['latitude']
lon = data.variables['longitude']
time = data.variables['time']
tx = data.variables['tx']

time_data=data.variables['time'][:]

lat_data=data.variables['latitude'][:]
lon_data=data.variables['longitude'][:]


cities=pd.read_excel('Cities.xlsx', sheet_name='LT', engine='openpyxl')


for index, row in cities.iterrows():
    print(row['Name'])




for index, row in cities.iterrows():
    location = (row['Name'])
    location_latitude = (row['Latitude'])
    location_longitude = (row['Longitude'])


    sq_diff_lat = (lat_data - location_latitude)**2
    sq_diff_lon = (lon_data - location_longitude)**2
    
    min_index_lat = sq_diff_lat.argmin()
    min_index_lon = sq_diff_lon.argmin()
    
    temp=data.variables['tx']
    
    
    
    
    data.variables['time']
    
    
    data.variables['time'].units[11:21]
    
    #Creating an empty pandas dataframe
    starting_date = data.variables['time'].units[11:21]
    ending_date = '2020-12-31'
    
    date_range = pd.date_range(start= starting_date, end=ending_date)
    df= pd.DataFrame(0,columns = ['tx'], index= date_range)
    
    
    data.variables['time'].size
    dt = np.arange(0, data.variables['time'].size)
    
    
    for time_index in dt: 
        df.iloc[time_index] = temp[time_index, min_index_lat,min_index_lon]
    
    
    
    df.to_csv(location +'.csv')


#TN#
data = Dataset(r'C:\Users\silva\Desktop\Carlo\9. Dati Pesanti\ECA&D\23.1\tn_ens_mean_0.25deg_reg_v23.1e.nc', 'r')

lat = data.variables['latitude']
lon = data.variables['longitude']
time = data.variables['time']
tn = data.variables['tn']

time_data=data.variables['time'][:]

lat_data=data.variables['latitude'][:]
lon_data=data.variables['longitude'][:]


cities=pd.read_excel('Cities.xlsx', sheet_name='LT', engine='openpyxl')


for index, row in cities.iterrows():
    print(row['Name'])




for index, row in cities.iterrows():
    location = (row['Name'])
    location_latitude = (row['Latitude'])
    location_longitude = (row['Longitude'])


    sq_diff_lat = (lat_data - location_latitude)**2
    sq_diff_lon = (lon_data - location_longitude)**2
    
    min_index_lat = sq_diff_lat.argmin()
    min_index_lon = sq_diff_lon.argmin()
    
    temp=data.variables['tn']
    
    
    
    
    data.variables['time']
    
    
    data.variables['time'].units[11:21]
    
    #Creating an empty pandas dataframe
    starting_date = data.variables['time'].units[11:21]
    ending_date = '2020-12-31'
    
    date_range = pd.date_range(start= starting_date, end=ending_date)
    df= pd.DataFrame(0,columns = ['tn'], index= date_range)
    
    
    data.variables['time'].size
    dt = np.arange(0, data.variables['time'].size)
    
    
    for time_index in dt: 
        df.iloc[time_index] = temp[time_index, min_index_lat,min_index_lon]
    
    
    
    df.to_csv(location +'.csv')


#RR#
data = Dataset(r'C:\Users\silva\Desktop\Carlo\9. Dati Pesanti\ECA&D\23.1\rr_ens_mean_0.25deg_reg_v23.1e.nc', 'r')

lat = data.variables['latitude']
lon = data.variables['longitude']
time = data.variables['time']
rr = data.variables['rr']

time_data=data.variables['time'][:]

lat_data=data.variables['latitude'][:]
lon_data=data.variables['longitude'][:]


cities=pd.read_excel('Cities.xlsx', sheet_name='LT', engine='openpyxl')


for index, row in cities.iterrows():
    print(row['Name'])




for index, row in cities.iterrows():
    location = (row['Name'])
    location_latitude = (row['Latitude'])
    location_longitude = (row['Longitude'])


    sq_diff_lat = (lat_data - location_latitude)**2
    sq_diff_lon = (lon_data - location_longitude)**2
    
    min_index_lat = sq_diff_lat.argmin()
    min_index_lon = sq_diff_lon.argmin()
    
    temp=data.variables['rr']
    
    
    
    
    data.variables['time']
    
    
    data.variables['time'].units[11:21]
    
    #Creating an empty pandas dataframe
    starting_date = data.variables['time'].units[11:21]
    ending_date = '2020-12-31'
    
    date_range = pd.date_range(start= starting_date, end=ending_date)
    df= pd.DataFrame(0,columns = ['rr'], index= date_range)
    
    
    data.variables['time'].size
    dt = np.arange(0, data.variables['time'].size)
    
    
    for time_index in dt: 
        df.iloc[time_index] = temp[time_index, min_index_lat,min_index_lon]
    
    
    
    df.to_csv(location +'.csv')


#QQ#
data = Dataset(r'C:\Users\silva\Desktop\Carlo\9. Dati Pesanti\ECA&D\23.1\qq_ens_mean_0.25deg_reg_v23.1e.nc', 'r')

lat = data.variables['latitude']
lon = data.variables['longitude']
time = data.variables['time']
qq = data.variables['qq']

time_data=data.variables['time'][:]

lat_data=data.variables['latitude'][:]
lon_data=data.variables['longitude'][:]


cities=pd.read_excel('Cities.xlsx', sheet_name='LT', engine='openpyxl')


for index, row in cities.iterrows():
    print(row['Name'])




for index, row in cities.iterrows():
    location = (row['Name'])
    location_latitude = (row['Latitude'])
    location_longitude = (row['Longitude'])


    sq_diff_lat = (lat_data - location_latitude)**2
    sq_diff_lon = (lon_data - location_longitude)**2
    
    min_index_lat = sq_diff_lat.argmin()
    min_index_lon = sq_diff_lon.argmin()
    
    temp=data.variables['qq']
    
    
    
    
    data.variables['time']
    
    
    data.variables['time'].units[11:21]
    
    #Creating an empty pandas dataframe
    starting_date = data.variables['time'].units[11:21]
    ending_date = '2020-12-31'
    
    date_range = pd.date_range(start= starting_date, end=ending_date)
    df= pd.DataFrame(0,columns = ['qq'], index= date_range)
    
    
    data.variables['time'].size
    dt = np.arange(0, data.variables['time'].size)
    
    
    for time_index in dt: 
        df.iloc[time_index] = temp[time_index, min_index_lat,min_index_lon]
    
    
    
    df.to_csv(location +'.csv')

#PP#

data = Dataset(r'C:\Users\silva\Desktop\Carlo\9. Dati Pesanti\ECA&D\23.1\pp_ens_mean_0.25deg_reg_v23.1e.nc', 'r')

lat = data.variables['latitude']
lon = data.variables['longitude']
time = data.variables['time']
pp = data.variables['pp']

time_data=data.variables['time'][:]

lat_data=data.variables['latitude'][:]
lon_data=data.variables['longitude'][:]


cities=pd.read_excel('Cities.xlsx', sheet_name='LT', engine='openpyxl')


for index, row in cities.iterrows():
    print(row['Name'])




for index, row in cities.iterrows():
    location = (row['Name'])
    location_latitude = (row['Latitude'])
    location_longitude = (row['Longitude'])


    sq_diff_lat = (lat_data - location_latitude)**2
    sq_diff_lon = (lon_data - location_longitude)**2
    
    min_index_lat = sq_diff_lat.argmin()
    min_index_lon = sq_diff_lon.argmin()
    
    temp=data.variables['pp']
    
    
    
    
    data.variables['time']
    
    
    data.variables['time'].units[11:21]
    
    #Creating an empty pandas dataframe
    starting_date = data.variables['time'].units[11:21]
    ending_date = '2020-12-31'
    
    date_range = pd.date_range(start= starting_date, end=ending_date)
    df= pd.DataFrame(0,columns = ['pp'], index= date_range)
    
    
    data.variables['time'].size
    dt = np.arange(0, data.variables['time'].size)
    
    
    for time_index in dt: 
        df.iloc[time_index] = temp[time_index, min_index_lat,min_index_lon]
    
    
    
    df.to_csv(location +'.csv')

#HU#
data = Dataset(r'C:\Users\silva\Desktop\Carlo\9. Dati Pesanti\ECA&D\23.1\hu_ens_mean_0.25deg_reg_v23.1e.nc', 'r')

lat = data.variables['latitude']
lon = data.variables['longitude']
time = data.variables['time']
hu = data.variables['hu']

time_data=data.variables['time'][:]

lat_data=data.variables['latitude'][:]
lon_data=data.variables['longitude'][:]


cities=pd.read_excel('Cities.xlsx', sheet_name='LT', engine='openpyxl')


for index, row in cities.iterrows():
    print(row['Name'])




for index, row in cities.iterrows():
    location = (row['Name'])
    location_latitude = (row['Latitude'])
    location_longitude = (row['Longitude'])


    sq_diff_lat = (lat_data - location_latitude)**2
    sq_diff_lon = (lon_data - location_longitude)**2
    
    min_index_lat = sq_diff_lat.argmin()
    min_index_lon = sq_diff_lon.argmin()
    
    temp=data.variables['hu']
    
    
    
    
    data.variables['time']
    
    
    data.variables['time'].units[11:21]
    
    #Creating an empty pandas dataframe
    starting_date = data.variables['time'].units[11:21]
    ending_date = '2020-12-31'
    
    date_range = pd.date_range(start= starting_date, end=ending_date)
    df= pd.DataFrame(0,columns = ['hu'], index= date_range)
    
    
    data.variables['time'].size
    dt = np.arange(0, data.variables['time'].size)
    
    
    for time_index in dt: 
        df.iloc[time_index] = temp[time_index, min_index_lat,min_index_lon]
    
    
    
    df.to_csv(location +'.csv')
