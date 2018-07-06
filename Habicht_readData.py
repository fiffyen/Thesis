import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta

#----------------------------------------------------------------
#	Bereitet die Daten der Behörde auf
#	Passt den Zeitstempel an und speichert die Datei um
#----------------------------------------------------------------

path = '/home/vivi/Dokumente/Master/Master_Thesis/data/Daten/Habichtstraße/'
opath = '/home/vivi/Dokumente/Master/Master_Thesis/data/Daten/Habichtstraße/raw/'
file = '68HB_PM10_PM2-5_70MB_PM10.csv'

original = pd.read_csv(opath + file, delimiter=';', skiprows=[0,1,2], header=None,
                 names=['time','68HB_PM10', '68HB_PM25', '70MB_PM10','x1']) 
df = original.copy()

# Korrektur des Datenformat: Tausche , gegen . Separation
df['68HB_PM10'] = df['68HB_PM10'].str.replace(',','.')
df['68HB_PM25'] = df['68HB_PM25'].str.replace(',','.')
df['70MB_PM10'] = df['70MB_PM10'].str.replace(',','.')

df['68HB_PM10'] = df['68HB_PM10'].astype('float64')
df['68HB_PM25'] = df['68HB_PM25'].astype('float64')
df['70MB_PM10'] = df['70MB_PM10'].astype('float64')

# Korrektur des Zeitformat
datelist = []
for l in range(len(df['time'])):
    date = str(df['time'][l])
    print(date)
    day = date.split('.')[0].strip()
    month = date.split('.')[1].strip()
    year = date.split('.')[2].split(' ')[0].strip()
    hour = date.split(' ')[1].split(':')[0].strip()
    minute = date.split(' ')[1].split(':')[1].strip()

    datelist = (datetime.datetime(np.int(year), np.int(month), np.int(day), np.int(hour)-1, np.int(minute)))
    datelist.strftime('%d.%m.%Y %H:%M')
    df.set_value(l, 'x1', datelist)

df.set_index('x1')
df['x1'] = df['x1'][:] + timedelta(hours=1) # Korrektur der Umwandlung

# Speichert erzeugte Datei
df.to_csv(path + 'HU_2017-2018_HB68_MB79.csv', index=False, sep=';')










