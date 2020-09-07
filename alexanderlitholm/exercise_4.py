import numpy as np
import pandas as pd


num_to_nparray = list()
for i in range(0, 12):
    num_to_nparray.append(int(input("Please enter a number to the dataframe: ")))

nparray = np.array(num_to_nparray)
nparray = np.split(nparray, 3)
print(nparray)

data_frame = pd.DataFrame(data=nparray, index=["row1", "row2", "row3"], columns=["colum1", "column2", "column3", "column4"])
print(data_frame)
