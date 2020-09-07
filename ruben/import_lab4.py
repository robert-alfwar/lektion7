import pandas as pd
import numpy as np

a, b, c, d, e, f, g, h, i, j, k, l = 12, 34, 45, 56, 67, 45, 99, 77, 32, 96, 22, 132
list1 = [a, b, c, d, e, f]
list2 = [g, h, i, j, k, l]
np_array1 = np.asarray(list1)
np_array2 = np.asarray(list2)
dataframe = pd.DataFrame({'x':np_array1, 'y':np_array2})
dataframe.plot('x', 'y', kind='scatter')