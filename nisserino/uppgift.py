import numpy as np
import pandas as pd

sample_input = [1, 3, 5, 6, 8, 12, 77, 32, 99, 13, 42, 156]
array1 = np.array(sample_input[0:3])
array2 = np.array(sample_input[4:7])
array3 = np.array(sample_input[8:11])
print(type(array3))

df = pd.DataFrame({'Col1': array1, 'Col2': array2, 'Col3': array3})
print(df)