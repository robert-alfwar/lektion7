import numpy as np
import pandas as pd


num_to_nparray = list()
for i in range(0, 12):
    year = 2017 + (i // 4)
    quarter = 1 + (i % 4)
    num_to_nparray.append(int(input(f'Enter profit Q{quarter} year {year}: ')))

nparray = np.array(num_to_nparray)
nparray = np.split(nparray, 3)
print(nparray)

data_frame = pd.DataFrame(data=nparray, index=["2017", "2018", "2019"],
                          columns=["Q1", "Q2", "Q3", "Q4"])
print(data_frame)
