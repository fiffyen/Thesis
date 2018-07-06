from datetime import datetime as dt
import numpy as np
import pandas as pd
import os
import copy

# ===========================================================
#source path:
main = '/home/vivi/Dokumente/Master/Master_Thesis/data/Daten/LuftdatenInfo_Download/'
path_HU = '/home/vivi/Dokumente/Master/Master_Thesis/data/Daten/Habichtstraße/'
path_LD = '/home/vivi/Dokumente/Master/Master_Thesis/data/Daten/LuftdatenInfo_Download/combined/'

# -----------------------------------------------------------
# Sensoren
sensor1 = [353, 1682, 4104, 7563]          				# Habichtstraße
sensor2 = [413, 836, 2448, 2470, 2876, 3673, 4581, 4672, 9426, 10335]   # Max B.-Allee
sensor2 = [413, 836, 2448, 2470, 2876, 3673, 4672, 9426]    		# Max B.-Allee
sensor = sensor1 + sensor2
Names = ['68HB_PM10', '68HB_PM25','70MB_PM10']				# HU Stationsnamen

# -----------------------------------------------------------
# Habicht

HU = pd.read_csv(path_HU + 'HU_2017-2018_HB68_MB70.csv', delimiter=';', parse_dates=True)
del HU['time']
HU['x1'] = pd.to_datetime(HU['x1'])
HU.set_index('x1')

# -----------------------------------------------------------
# Luftdaten

# PM10
P1 = pd.read_csv(path_LD + 'P1_2017-2018_Luftdaten.csv', parse_dates=True, delimiter=';')
P1.set_index('time')
P1['time'] = pd.to_datetime(P1['time'])

# PM25
P2 = pd.read_csv(path_LD + 'P2_2017-2018_Luftdaten.csv', parse_dates=True, delimiter=';')
P2.set_index('time')
P2['time'] = pd.to_datetime(P2['time'])

# -----------------------------------------------------------
# Equalising Datasets based on the HU-Data.
time = HU['x1']
mask_time = (P1['time'] >= time.iloc[0]) & (P1['time'] <= time.iloc[-1])

P10 = copy.deepcopy(P1)
P10 = P10.loc[mask_time]
P10 = P10.reset_index(drop=True)

P25 = copy.deepcopy(P2)
P25 = P25.loc[mask_time]
P25 = P25.reset_index(drop=True)


# ===========================================================
# Functions:
def getTime(timeseries):
#   Convert Time into matplotlib readable format for the x-axis
#   timeseries = ['2013-7-1 05:10:00', '2013-7-1 05:20:00']
#   so sollte die Liste aussehen, die du uebergibst (diese Zeile brauchst du dann nicht mehr)
    datelist = []

    for date in timeseries:
        day = date.split('-')[2].split(' ')[0].strip()
        month = date.split('-')[1].strip()
        year = date.split('-')[0].strip()
        hour = date.split(' ')[1].split(':')[0].strip()
        minute = date.split(' ')[1].split(':')[1].strip()
        seconds = date.split(' ')[1].split(':')[2].strip()

        datelist.append(dt(np.int(year), np.int(month), np.int(day), np.int(hour), np.int(minute)))
    return (datelist)

# ===========================================================
# sort values 
def sortDate(file, pdtimename):
    df = pd.read_csv(file)
    df[pdtimename] = pd.to_datetime(df[pdtimename], dayfirst=True)  # , format='%d.%m.%y %H:%M')
    df = df.sort_values([pdtimename], ascending=[True])
    df = df.reset_index(drop=True)
    df = df.fillna('nan')
    return(df)

# ===========================================================
# Creates new folder
def create_folder(path, name):
    newpath = path + str(name)
    if not os.path.isdir(newpath):  # create Sensor folder
        os.makedirs(newpath)
      #  print('new folder: '+str(newpath))
    #else:
     #   print('folder exist: '+str(newpath))
    #return(newpath)


