import os.path
from datetime import datetime, time, timedelta
import pandas as pd

#---------------------------------------------------------------
#	Aufbereitung der Luftdaten auf 1H-Mittel
#---------------------------------------------------------------

# ===========================================
ipath = "/home/vivi/Dokumente/Master/Master_Thesis/data/LuftdatenInfo_Download/raw/"
path = "/home/vivi/Dokumente/Master/Master_Thesis/data/LuftdatenInfo_Download/"
sensor1 = [353, 1682, 4104, 7563]                                        # Habichtstraße
sensor2 = [413, 836, 2448, 2470, 2876, 3673, 4581, 4672, 9426, 10335]    # Max B.-Allee

sensor = sensor1 + sensor2
sensor = [4581]

start_date = "2018-03-19"
stop_date = "2018-03-20"

# =======================================

start = datetime.strptime(start_date, "%Y-%m-%d")
stop = datetime.strptime(stop_date, "%Y-%m-%d")


# create Sensor folder
for s in sensor:
    if not os.path.isdir(path + str(s)):
        os.makedirs(path + str(s) + '/1h/')

while start <= stop:
    datum = start.date()
    print(datum)
    for s in sensor:
        file = str(ipath) + str(s)+ '/' + str(datum)+'_sds011_sensor_'+str(s) + '.csv'
        #out_file = str(path) + str(s)+ '/' + str(datum)+'_sds011_sensor_VV_'+str(s) + '.csv'
        print(file)

        if os.path.isfile(file):
            print('exist')
            df = pd.read_csv(file, delimiter=';', parse_dates=True)
            df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y%m%dT%H:%M:%S')
            data = df.set_index('timestamp')
            #data.to_csv(out_file, index=True)
            for i in ['durP1','ratioP1', 'durP2', 'ratioP2', 'sensor_type']:
                del data[i]

            print(data['P1'])
            rest = data['P1'].resample('60Min')
            print(rest)
            print(rest.mean())
            print(data['P1'].resample('60Min').mean())
            b = data.resample('60Min').mean()
            #b.to_csv(path  + str(s) + '/1h/' + str(datum) + '_sds011_sensor_' + str(s) + '_mean-1h.csv', sep=';')

        else:
            print('nope')
    start = start + timedelta(days=1)




print('\nmean Luftdaten done')
