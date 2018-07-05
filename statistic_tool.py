import numpy as np
import copy


def statistic(sens, P, O):
    print('sensor ' + str(sens))
    O1 = copy.deepcopy(O)
    P1 = copy.deepcopy(P)
    #print(O1.head(), P1.head())

    error = P1 - O1
    #print(error)
    p10 = np.nanpercentile(error, 10)
    p50 = np.nanpercentile(error, 50)
    p90 = np.nanpercentile(error, 90)
    print('p10: ' + str(p10))
    print('p50: ' + str(p50))
    print('p90: ' + str(p90))

    # Bias
    bias = np.nanmean(P1) - np.nanmean(O1)
    print('BIAS: ' + str(bias))
    # RMSE
    rmse = np.sqrt(np.nanmean(((P1 - O1) ** 2)))
    print('RMSE: ' + str(rmse))

    # Correlation
    cor = np.corrcoef(P1, O1)
    print('CORR: ' + str(cor[0])+ '\n')

    """        
    # Hit rates
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

#statistic(sensor1, P1, HU[sensorH[0]])
