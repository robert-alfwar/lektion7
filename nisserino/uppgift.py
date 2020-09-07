import numpy as np
import pandas as pd

# note: missing user input
sample_input = [1, 3, 5, 6, 8, 12, 77, 32, 99, 13, 42, 156]
array1 = np.array(sample_input[0:3])
array2 = np.array(sample_input[4:7])
array3 = np.array(sample_input[8:11])
# note: missing 1 row

df = pd.DataFrame(data=[array1, array2, array3],
                  columns=['2017', '2018', '2019'],
                  index=['Q1', 'Q2', 'Q3'])
print(df)
