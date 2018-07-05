import pandas as pd
import numpy as np

#------------------------------------------------------------------------
# Überprüfung der Sensor Location auf Änderung der Kennziffer
#------------------------------------------------------------------------


sensor1 = [353, 1682, 4104, 7563]                                        # Habichtstraße
sensor2 = [413, 836, 2448, 2470, 2876, 3673, 4581, 4672, 9426, 10335]    # Max-Brauer
sensor = sensor1 + sensor2

inpath = '/home/vivi/Dokumente/Master/Master_Thesis/data/Daten/LuftdatenInfo_Download/combined/'

for s in sensor:
    file = '2017-2018_sds011_sensor_' +str(s) + '_mean-1h.csv'
    P1 = pd.read_csv(inpath + file, parse_dates=True, delimiter=';')
    print(s)
    check = P1['location'].loc[0]
    print(check)
    mask = (P1['location'] != check) # & (P1['location'] == np.nan)
    dfL = P1['location'].loc[mask]
    print(dfL)
    print(' \n\n')
