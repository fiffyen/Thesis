import os.path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, time, timedelta
from Utilities import create_folder, sortDate, sensor1, sensor2, sensor, main

# ===========================================
resample_interval = '60Min'

inpath = main

raw = inpath +"raw/"
res = inpath + resample_interval +'/'
com = inpath + '/combined/'

start_date = "2017-03-20"
stop_date = "2018-03-20"
stime = time(0, 0, 0)  # Create Timestamp
etime = time(23, 59, 59)

# SEE CALL FUNCTIONS DOWN
# =======================================

# A. Do the resample for preparing downloaded data for merging
def do_resample(day, pin, pout, x):
    create_folder(pout, x)             # create Folder
    datum = day.date()                # for filename
    file = str(pin) + str(x)+ '/' + str(datum)+'_sds011_sensor_'+str(x) + '.csv'

    if os.path.isfile(file):            # check if file exists
        df = pd.read_csv(file, delimiter=';', parse_dates=True)
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y%m%dT%H:%M:%S')
        data = df.set_index('timestamp')
        for i in ['durP1','ratioP1', 'durP2', 'ratioP2', 'sensor_type']:
            del data[i]
        b = data.resample('60Min').mean()
        b.to_csv(pout + '/' + str(x) + '/' + str(datum) + '_sds011_sensor_' + str(x) + '_mean-1h.csv', sep=';')

def resample(sdate, edate, sens, pin, pout):
    start = datetime.strptime(sdate, "%Y-%m-%d")
    stop = datetime.strptime(edate, "%Y-%m-%d")
    while start <= stop:
        for s in sens:
            do_resample(start, pin, pout, s)
        start = start + timedelta(days=1)
    print('\nmean Luftdaten done')


# B. Merging Files
def merge_daily(pin, pout, sens):
    for s in sens:
        print(s)
        path = pin + str(s) + '/'
        file = os.listdir(path)
        df0 = pd.read_csv(path+file[0], delimiter=';', parse_dates=True)    # grab first file in list
        for f in range(1, len(file)):                                       # for each remaining file append to f0
            dff = pd.read_csv(path + file[f], delimiter=';', parse_dates=True)
            df0 = df0.append(dff, ignore_index=True)

        df0 = df0.sort_values(['timestamp'], ascending=[True])
        df0 = df0.reset_index(drop=True)
        df0 = df0.fillna('nan')

        name = '2017-2018_sds011_sensor_' + str(s) + '_mean-1h.csv'
        df0.to_csv(pout + name,sep=';', index=False)
    print('merge done')

def plot_daily(pout):
    files = os.listdir(pout)
    newlist = []
    for item in files:
        if item.endswith(".csv"):
            newlist.append(item)
    for f in newlist:
        print(f)
        df = pd.read_csv(pout + f, delimiter=';', parse_dates=True)
        df.set_index('timestamp')

        df.plot(y=['P1', 'P2'], x='timestamp',
                use_index=True,
                figsize=(20, 12),
                title=(str(f)))

        name = str(f).split('.')[0] + '.png'
        plt.savefig(pout + name)
        plt.close()


def time(sdate, edate):
    start = datetime.strptime(sdate, "%Y-%m-%d")
    stop = datetime.strptime(edate, "%Y-%m-%d")
    realstart = datetime.combine(start, stime)  # Combine separatet date and time to get datetime
    realend = datetime.combine(stop, etime)
    delta = timedelta(hours=1)

    temp = []
    while realstart <= realend:
        temp.append(realstart)
        realstart += delta
    df = pd.DataFrame(data=temp, columns = ['time'])
    df['time'] = pd.to_datetime(df['time'], format='%Y%m%dT%H:%M:%S')
    #df = df.set_index('time')
    #df.to_csv('time.csv')
    return(df)


# C. Merge all
def merge_all(sdate, edate, sens, pin):
    times = time(sdate, edate)
    for s in sens:
        times[str(s)] = np.nan
    P1 = times.copy()
    P2 = times.copy()

    files = os.listdir(pin)
    newlist = []
    for item in files:
        if item.endswith(".csv"):
            newlist.append(item)

    for s in sens:
        for f in newlist:
            if f.endswith(str(s) + '_mean-1h.csv'):
                print(s, f)  # Kontrolle
                df = pd.read_csv(pin + f, delimiter=';', parse_dates=True)
                df.set_index('timestamp')
                for t in range(len(df)):
                    o = df['timestamp'][t]  # take timestamp for each input csv
                    p = times.loc[times['time'] == o].index  # compare timestamp with alltimes-csv
                    P1.set_value(p[0], str(s), df['P1'][t])  # write values from input into merged time-csv
                    P2.set_value(p[0], str(s), df['P2'][t])

    P1['time'] = pd.to_datetime(P1['time'], format='%Y%m%dT%H:%M:%S')
    P1['time'] = P1['time'][:] + timedelta(hours=1)
    P1.to_csv(pin + 'P1_2017-2018_Luftdaten.csv', index=False, sep=';')
    P2['time'] = P2['time'][:] + timedelta(hours=1)
    P2['time'] = pd.to_datetime(P2['time'], format='%Y%m%dT%H:%M:%S')
    P2.to_csv(pin + 'P2_2017-2018_Luftdaten.csv', index=False, sep=';')

# =======================================
# CALL FUNCTIONS

#resample(start_date, stop_date, sensor, raw, res)
#merge_daily(res, com, sensor)
#merge_all(start_date, stop_date, sensor, com)
