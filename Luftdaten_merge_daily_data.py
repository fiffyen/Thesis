import os.path
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from Utilities import create_folder, sortDate

# ===========================================
sensor1 = [353, 1682, 4104, 7563]                                        # Habichtstraße
sensor2 = [413, 836, 2448, 2470, 2876, 3673, 4581, 4672, 9426, 10335]    # Max B.-Allee

inpath = '/home/vivi/Dokumente/Master/Master_Thesis/data/LuftdatenInfo_Download'
sensor = sensor1 + sensor2

# ===========================================

outpath = inpath + '/combined/'


for s in sensor:
    path = inpath + '/' + str(s) + '/1h/'
    opath = outpath
    file = os.listdir(path)
    df0 = pd.read_csv(path+file[0], delimiter=';', parse_dates=True)
    for f in range(1, len(file)):
        dff = pd.read_csv(path + file[f], delimiter=';', parse_dates=True)
        df0 = df0.append(dff, ignore_index=True)

    df0 = df0.sort_values(['timestamp'], ascending=[True])
    df0 = df0.reset_index(drop=True)
    df0 = df0.fillna('nan')

    name = '2017-2018_sds011_sensor_' + str(s) + '_mean-1h.csv'
    df0.to_csv(opath + name,sep=';', index=False,)

    #/home/vivi/Dokumente/Master/Master_Thesis/data/LuftdatenInfo_Download/353/1h/2017-03-27_sds011_sensor_353_mean-1h.csv


files = os.listdir(opath)
newlist = []
for item in files:
    if item.endswith(".csv"):
        newlist.append(item)

for f in newlist:
    print(f)
    df = pd.read_csv(opath + f, delimiter=';', parse_dates=True)
    df.set_index('timestamp')


    df.plot(y=['P1', 'P2'], x='timestamp',
            use_index=True,
            figsize=(20, 12),
            title=(str(f)))

    name = str(f).split('.')[0] + '.png'
    plt.savefig(opath + name)
#    plt.show()
