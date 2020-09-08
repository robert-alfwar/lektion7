import pandas as pd
import numpy as np

a = [int(x) for x in input("Enter 12 numbers seperated by space: ").split()]
print(a)

npArr = np.array(a)
print('Numpy array: ', npArr)

npArr = np.split(npArr, 3)
pd_df = pd.DataFrame(npArr)
print('Pandas dataframe: ')
print(pd_df)