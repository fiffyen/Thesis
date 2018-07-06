import numpy as np
import pandas as pd
#--------------------------------------------------------
path = "/home/vivi/Dokumente/Master/Master_Thesis/data/"
file = "m3tras_TAPE80"
outfile = "m3tras_TAPE80_nowater"
Hrow = 7   # Amount of header rows
Frow = -1
#--------------------------------------------------------

# Process The Header & Footer
# write Headertext out in to a list
# Adding later to the file

headertext = [] 
footertext = []
f = open(path+file, 'r')
a = f.readlines()
i = 0
j = -3
while i <= Hrow:
    headertext.append(a[i])
    i +=1
while j <= Frow:
    footertext.append(a[j])
    j +=1


# Code:

data = np.genfromtxt(path+file, skip_header=Hrow+1, skip_footer=3, dtype=None)
df = pd.DataFrame(data=data)
lastnum = int(df.iloc[-1,0])
print(df.head())
print(lastnum)

extent = []
n = lastnum +1
k = 1
for i in range(51,61):
    for j in range(5,47):
        if i == 51 or i == 60:
            e = 6.7E-09        
        else:
            e = 1.0E-08
        extent.append([n, i, j, k, e])
        n +=1

    for j in range(58,132):
        if i == 51 or i == 60:
            e = 6.7E-09        
        else:
            e = 1.0E-08
        extent.append([n, i, j, k, e])
        n +=1
        
ex = pd.DataFrame(data=extent)
ex.columns = ['f0', 'f1', 'f2', 'f3', 'f4']

lastnum2 = int(ex.iloc[-1,0])
print(ex.head())
print(lastnum, lastnum2)

together = pd.concat([df, ex], ignore_index=True)
print(together.tail())

Infoline = a[6].replace('1298', str(lastnum2))
print(Infoline)
headertext[6] = Infoline

# Write output        
with open(path+outfile, 'w') as out:
    for line in headertext:
        out.write(line)
    together.to_csv(out, index=False, header=False, sep ='\t')
    for line in footertext:
        out.write(line)
        
        
        
        



