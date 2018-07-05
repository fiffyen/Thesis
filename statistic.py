import pandas as pd
import numpy as np
import copy

sensor1 = [353, 1682, 4104, 7563]                                        # Habichtstraße
sensor2 = [413, 836, 2448, 2470, 2876, 3673, 4581, 4672, 9426, 10335]    # Max B.-Allee
sensorH = ['68HB_PM10', '68HB_PM25', '70MB_PM10']


inpath = '/home/vivi/Dokumente/Master/Master_Thesis/data/LuftdatenInfo_Download/combined/'
sensor = sensor1 + sensor2

hu = '/home/vivi/Dokumente/Master/Master_Thesis/data/Habichtstraße/HU_2017-2018_HB68_MB79.csv'
Lp1 = 'P1_2017-2018_Luftdaten.csv'
Lp2 = 'P2_2017-2018_Luftdaten.csv'

P1 = pd.read_csv(inpath + Lp1,  delimiter=';', parse_dates=True)
P2 = pd.read_csv(inpath + Lp2,  delimiter=';', parse_dates=True)
HU = pd.read_csv(hu,  delimiter=';', parse_dates=True)

def statistic(sens, pm, org):
    for x in sens:
        print(str(x))
        orig = copy.deepcopy(org)
        item = copy.deepcopy(pm[str(x)])
        #print(orig.head(), item.head())

        error = item - orig
        #print(error)
        p10 = np.nanpercentile(error, 10)
        p50 = np.nanpercentile(error, 50)
        p90 = np.nanpercentile(error, 90)
        print('p10: ' + str(p10))
        print('p50: ' + str(p50))
        print('p90: ' + str(p90))

        # Bias
        bias = np.nanmean(item) - np.nanmean(orig)
        print('BIAS: ' + str(bias))
        # RMSE
        rmse = np.sqrt(np.nanmean(((item - orig) ** 2)))
        print('RMSE: ' + str(rmse))


statistic(sensor1, P1, HU[sensorH[0]])
statistic(sensor1, P2, HU[sensorH[1]])
statistic(sensor2, P1, HU[sensorH[2]])


# Correlation
#cor = np.corrcoef(P2, O2)
#print('CORR: ' + str(cor))
# Hit rates
"""

H = 0
for j in range(len(O2)):
    if name == var_name[0] and abs((P2[j] - O2[j]) / O2[j]) <= 0.02:
        H += 1.
    elif name == var_name[1] and abs((P2[j] - O2[j]) / O2[j]) <= 0.10:
        H += 1.
    else:
        H += 0

if len(O2) == 0:
    print('no Hitrate')
else:
    H = H / len(O2)
    print('Hitrate: ' + str(H))

#plt.plot(date, itemp - x250temp)
print(' ')
"""

