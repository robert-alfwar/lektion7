import numpy as np
import pandas as pd


data = list(input("Enter 12 numbers separated by , >> ").strip().split(','))

# sample_input = [1, 3, 5, 6, 8, 12, 77, 32, 99, 13, 42, 156]
array1 = np.array(data[0:4])
array2 = np.array(data[4:8])
array3 = np.array(data[8:12])

df = pd.DataFrame(data=[array1, array2, array3],
                  index=['2017', '2018', '2019'],
                  columns=['Q1', 'Q2', 'Q3', 'Q4'])
print(df)
