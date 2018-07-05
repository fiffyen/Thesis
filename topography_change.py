import numpy as np
import pandas as pd

#--------------------------------------------------------
path = "/home/vivi/Dokumente/Master/Master_Thesis/data/Top/"
file = "GA_e30v0bb"
outfile = "GA_e30v0bb_nowater"

Hrow = 17   # Amount of header rows
#--------------------------------------------------------

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

# Header of Dataframe
columns = ['ii', 'ij', 'ydx', 'ydy', 'zsurf', '1100', '2107', '2220', '2230', '3100', '3500', 'x', 'y']
columns.remove('1100')

# Read and processing data
data = np.genfromtxt(path+file, skip_header=Hrow+1, dtype=None)
df = pd.DataFrame(data=data)
df['f7'] = df['f5'] + df['f7']    # f5 + f7
del df['f5']                      # delete column f5
print(df)

# create outputfile
with open(path+outfile, 'w') as out:
    for line in headertext:
        out.write(line)
    df.to_csv(out, index=False, header=False, sep ='\t')


