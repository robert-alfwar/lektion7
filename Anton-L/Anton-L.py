import pandas as pd
import numpy as np

talen = []
for i in range(1, 13):
    talen.append(int(input(f'Ange tal {i}: ')))

np_arrays = np.array_split(np.array(talen), 3)

pd_table = pd.DataFrame(data=np_arrays, index=['2020', '2019', '2018'], columns=['Q1', 'Q2', 'Q3', 'Q4'])
print(f'\n{pd_table}')
