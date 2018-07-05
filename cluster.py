from Utilities import P_1, P_2, HU, sensor1, sensor2
import pandas as pd


df_weekdays = HU.resample('B').mean()

print(df_weekdays)

