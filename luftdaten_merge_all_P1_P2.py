import os.path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import timedelta

sensor1 = [353, 1682, 4104, 7563]                                        # Habichtstraße
sensor2 = [413, 836, 2448, 2470, 2876, 3673, 4581, 4672, 9426, 10335]    # Max B.-Allee
inpath = '/home/vivi/Dokumente/Master/Master_Thesis/data/LuftdatenInfo_Download/combined/'

sensor = sensor1 + sensor2

times = pd.read_csv('time.csv', parse_dates=True)
times.set_index('time')
for s in sensor:
    times[str(s)] = np.nan

P1 = times.copy()
P2 = times.copy()

files = os.listdir(inpath)
newlist = []
for item in files:
    if item.endswith(".csv"):
        newlist.append(item)

# 2017-2018_sds011_sensor_4581_mean-1h.csv   # Filename
for s in sensor:
    for f in newlist:
        if f.endswith(str(s)+'_mean-1h.csv'):
            print(s,f)                                          # Kontrolle
            df = pd.read_csv(inpath + f, delimiter=';',parse_dates=True)
            df.set_index('timestamp')

            # combine all values for each PM into one csv-file: get same size for comparison plot
            for t in range(len(df)):
                o = df['timestamp'][t]                          # take timestamp for each input csv
                p = times.loc[times['time'] == o].index         # compare timestamp with alltimes-csv
                P1.set_value(p[0], str(s), df['P1'][t])         # write values from input into merged time-csv
                P2.set_value(p[0], str(s), df['P2'][t])


P1['time'] = pd.to_datetime(P1['time'], format='%Y%m%dT%H:%M:%S')
P2['time'] = pd.to_datetime(P2['time'], format='%Y%m%dT%H:%M:%S')

P1['time'] = P1['time'][:] + timedelta(hours=1)
P2['time'] = P2['time'][:] + timedelta(hours=1)



P1.to_csv(inpath + 'P1_2017-2018_Luftdaten.csv', index=False, sep=';')
P2.to_csv(inpath + 'P2_2017-2018_Luftdaten.csv', index=False, sep=';')
