import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ============================
# For Weekly plotting:
start_date = "2017-03-20"
stop_date = "2018-03-19"
delta = timedelta(weeks=1)

# ============================
# Sensor names:
sensor1 = [353, 1682, 4104, 7563]                                        # Habichtstraße
sensor2 = [413, 836, 2448, 2470, 2876, 3673, 4581, 4672, 9426, 10335]    # Max B.-Allee
sensor = sensor1 + sensor2
labels = [str(i) for i in sensor]

# ============================
# Paths
inpath = '/home/vivi/Dokumente/Master/Master_Thesis/data/LuftdatenInfo_Download/combined/'
path = '/home/vivi/Dokumente/Master/Master_Thesis/data/Habichtstraße/'
weeklyp = '/home/vivi/Dokumente/Master/Master_Thesis/data/Weekly/'

# ============================
# HU DATA
HU = pd.read_csv(path + 'HU_2017-2018_HB68_MB79.csv', delimiter=';', parse_dates=True)
del HU['time']
HU['x1'] = pd.to_datetime(HU['x1'])
HU.set_index('x1')

# LUFTDATA
# PM10
P1 = pd.read_csv(inpath + 'P1_2017-2018_Luftdaten.csv', parse_dates=True, delimiter=';')
P1.set_index('time')
P1['time'] = pd.to_datetime(P1['time'])
# PM25
P2 = pd.read_csv(inpath + 'P2_2017-2018_Luftdaten.csv', parse_dates=True, delimiter=';')
P2.set_index('time')
P2['time'] = pd.to_datetime(P2['time'])

# ============================
# Ganzer Zeitraum:
# Habichtstraße
for s in sensor1:
    ax = P1.plot(y=str(s), x='time', figsize=(20,12), label='PM10', title=str(s))
    P2.plot(y=str(s), x='time', ax=ax , label='PM2.5')
   # HU.plot(y='68HB_PM10', ax=ax)
   # plt.savefig(inpath+'LUFT_HU_2017-2018_sds011_sensor_' + str(s)+'_mean-1h.png')
    plt.close()

# Max Brauer Allee
for s in sensor2:
    ax = P1.plot(y=str(s), x='time', figsize=(20,12), label='PM10', title=str(s))
    P2.plot(y=str(s), x='time', ax=ax , label='PM2.5')
    #HU.plot(y='70MB_PM10', ax=ax)
   # plt.savefig(inpath+'LUFT_HU_2017-2018_sds011_sensor_' + str(s)+'_mean-1h.png')
    plt.close()

# ============================
# pLOT per week:


start = datetime.strptime(start_date, "%Y-%m-%d")
stop = datetime.strptime(stop_date, "%Y-%m-%d")

while start <= stop:

    a = str(start).split(' ')[0].strip()
    e = str(start + delta).split(' ')[0].strip()
    print(s,e)

    for s in sensor1:
        mask = (P1['time'] >= start) & (P1['time'] < start+delta)
        dfL = P1.loc[mask]
        dfL2 = P2.loc[mask]
        mask = (HU['x1'] >= start) & (HU['x1'] < start + delta)
        dfH = HU.loc[mask]

        title = 'Habichtstrasse ' + str(s) + ': ' + str(dfL['time'].iloc[0]) + ' - ' + str(dfL['time'].iloc[-1])
        ax = dfL.plot(y=str(s), x='time', figsize = (20, 12), label = 'PM10', title=title) # title = str(s[0]))
        dfL2.plot(y=str(s), x='time', ax=ax, label='PM2.5')
        dfH.plot(y='68HB_PM10', x='x1', ax=ax, label='HU PM10')
        dfH.plot(y='68HB_PM25', x='x1', ax=ax, label='HU PM2.5')
       # plt.savefig(weeklyp + 'Habicht_' + str(s) +'_' + str(a) + '-' + str(e) + '.png')
        plt.close()

    for s in sensor2:
        mask = (P1['time'] >= start) & (P1['time'] < start+delta)
        dfL = P1.loc[mask]
        dfL2 = P2.loc[mask]
        mask = (HU['x1'] >= start) & (HU['x1'] < start + delta)
        dfH = HU.loc[mask]

        title = 'Max-Brauer-Allee ' + str(s) + ': ' + str(dfL['time'].iloc[0]) + ' - ' + str(dfL['time'].iloc[-1])
        ax = dfL.plot(y=str(s), x='time', figsize = (20, 12), label = 'PM10', title=title) # title = str(s[0]))
        dfL2.plot(y=str(s), x='time', ax=ax, label='PM2.5')
        dfH.plot(y='70MB_PM10', x='x1', ax=ax, label='HU PM10')
       # plt.savefig(weeklyp + 'MaxBrauer_' + str(s) +'_' + str(a) + '-' + str(e) + '.png')
        plt.close()

    start += delta




