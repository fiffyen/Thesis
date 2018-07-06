import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = '/home/vivi/Dokumente/Master/Master_Thesis/data/TAPES/m3tras_TAPE80_idhb_b44b'
GA_file = '/home/vivi/Dokumente/Master/Master_Thesis/data/TAPES/GA_idHB_g6k30_b44b_ne'

ga = open(GA_file, 'r')
lines = list(ga)

print(lines[-1])

data = np.genfromtxt(file, skip_header=8, skip_footer=3, dtype=None)
tape = pd.DataFrame(data=data)
print(tape.head())

print(tape['f1'].min(), tape['f1'].max())   #ii
print(tape['f2'].min(), tape['f2'].max())   #ij



nrows, ncols = 151,173      # ii, ij
image = np.zeros(nrows*ncols)
image = image.reshape((nrows, ncols)) # Reshape things into a 9x9 grid.

for i in range(len(tape)):
    #print(tape['f1'][i], tape['f2'][i])
    x = (tape['f2'][i])
    y = (tape['f1'][i])
    image[x,y] = tape['f4'][i]

plt.matshow(image)
plt.show()

"""
row_labels = range(nrows)
col_labels = range(ncols)

plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)
"""
