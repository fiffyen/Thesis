import numpy as np
import pandas as pd
#--------------------------------------------------------

path = '/home/vivi/Dokumente/Master/Master_Thesis/data/Top/'
file = "GA_e30v0bb_nowater"

Hrow = 17   # Amount of header rows

# Process The Header
headertext = []

# write Headertext out in to a list
# Adding later to the file
f = open(path+file, 'r')
i = 0
while i <= Hrow:
    headertext.append(f.readline())
    i +=1
print(headertext)

cols = ['ii', 'ij', 'ydx', 'ydy', 'zsurf', '2107', '2220', '2230', '3100', '3500', 'x', 'y']
data = np.genfromtxt(path+file, skip_header=Hrow+1, dtype=None)
df = pd.DataFrame(data=data)#, columns=cols)
df.columns = cols
#print(df.head())

mask = (df['ij'] == 52)
dfL2 = df.loc[mask]
#pd.DataFrame(np.where(np.logical_or(np.isnan(m), m > 0), np.tile(m[:, [4]], 5), m),
columns=df.columns(np.where(np.logical_or(np.isnan(m), m > 0), np.tile([:, [4]], 5), m))
#columns=df.columns
print(dfL2)


#mask = (df['ij'] >= 51) & (df['ij'] <= 53)
#i = df.loc[mask].index




"""
dfL = df['3100'].loc[mask]
df = df.where(mask, other=30)

for t in range(len(dfL)):
    o = df['3100'][t]  # take timestamp for each input csv
    p = times.loc[times['time'] == o].index  # compare timestamp with alltimes-csv
    # print(o, p[0], f)
    P1.set_value(p[0], str(s), df['P1'][t])  # write values from input into merged time-csv
    P2.set_value(p[0], str(s), df['P2'][t])


#dfL2 = P2.loc[mask]
#mask = (HU['x1'] >= start) & (HU['x1'] < start + delta)
print(dfL)
"""