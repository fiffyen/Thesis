from Utilities import P10, P25, HU, sensor1, sensor2
import pandas as pd
import statistic_tool as st
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pylab
import copy

Plot_path = '/home/vivi/Dokumente/Master/Master_Thesis/data/Plots/scatter/'

def scat_q(sens, p, h, n):
    for s in sens:
        print('sensor ' + str(s))

        # Preparation:
        # Ignore Lines where Luftdaten.info data is nan
        mask = np.where(np.invert(np.isnan(p[str(s)])))
        DF = p[str(s)].loc[mask[0]]
        UH = h[n].loc[mask[0]]
        UH = UH.reset_index(drop=True)
        DF = DF.reset_index(drop=True)
        print(len(UH), len(DF))

        # Ignore Lines where HU data is nan
        mask = np.where(np.invert(np.isnan(UH)))
        DF2 = DF.loc[mask[0]]
        UH2 = UH.loc[mask[0]]
        UH2 = UH2.reset_index(drop=True)
        DF2 = DF2.reset_index(drop=True)
        print(len(UH2), len(DF2))
        print(' ')


        # Apply statistics on prepared data
        st.statistic(s, DF2, UH2)


        # ---- PLOT -----
        # create scatterplot
        plt.scatter(UH2, DF2, color='b')
        plt.xlabel(str(n))
        plt.ylabel(str(s))
        #plt.savefig(path + 'scatter_' +str(s) + '.png')
        plt.close()

#        stats.probplot(UH2, dist="norm", plot=pylab)
#        plt.title(str(n))
#        plt.savefig(path + 'probplot_' +str(n) + '.png')
#        plt.close()


        # Percentile Plot
        PObs = np.zeros(100)
        PMod = np.zeros(100)

        for i in range(100):
            PObs[i] = np.nanpercentile(UH2, i + 1)
            PMod[i] = np.nanpercentile(DF2, i + 1)  # -ff[0,j+1,:],i+1)

        plt.plot(PObs, PMod, 'o', color='b')
        plt.ylabel(str(s))
        plt.xlabel(n)
        #plt.savefig(path + 'quantile_' + str(s) + '.png')
        plt.close()
        print(' ')


# ------- Call Functions ---------
scat_q(sensor1, P_1, HU, '68HB_PM10')
scat_q(sensor1, P_2, HU, '68HB_PM25')
scat_q(sensor2, P_1, HU, '70MB_PM10')





