import os.path
from datetime import datetime, time, timedelta
import pandas as pd

#------------------------------------------------------------------------
#	Erzeugt Gewichtetes Mittel der Daten
#------------------------------------------------------------------------

# ===========================================
ipath = "/home/vivi/Dokumente/Master/Master_Thesis/data/LuftdatenInfo_Download/raw/"
#path = "/home/vivi/Dokumente/Master/Master_Thesis/data/LuftdatenInfo_Download/"
sensor1 = [353, 1682, 4104, 7563]                                        # Habichtstraße
sensor2 = [413, 836, 2448, 2470, 2876, 3673, 4581, 4672, 9426, 10335]    # Max B.-Allee

sensor = sensor1 + sensor2


start_date = "2017-03-19"
stop_date = "2018-03-28"

# =======================================

start = datetime.strptime(start_date, "%Y-%m-%d")
stop = datetime.strptime(stop_date, "%Y-%m-%d")


def wavg(group, avg_name, weight_name):
    """ http://stackoverflow.com/questions/10951341/pandas-dataframe-aggregate-function-using-multiple-columns
    In rare instance, we may not have weights, so just return the mean. Customize this if your business case
    should return otherwise.
    """
    d = group[avg_name]
    w = group[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()



while start <= stop:
    datum = start.date()
    print(datum)
    for s in sensor:
        file = str(ipath) + str(s)+ '/' + str(datum)+'_sds011_sensor_'+str(s) + '.csv'
        print(str(datum)+'_sds011_sensor_VV_'+str(s))

        if os.path.isfile(file):
            df = pd.read_csv(file, delimiter=';', parse_dates=True)
            df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y%m%dT%H:%M:%S')
            #time = df.iloc[:,5]
            #data = df.set_index('timestamp')
            #data.to_csv(out_file, index=True)

           # print(time)
           # df.groupby(df.Period('timestamp'))

            #sales["Current_Price"] * sales["Quantity"]).sum() / sales["Quantity"].sum()
            (df["timestamp"] * df["P1"]).sum() / df["timestamp"].sum()



        else:
            print('nope')

    start = start + timedelta(days=1)
    print(' ')




print('\nmean Luftdaten done')
