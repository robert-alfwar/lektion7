import pandas as pd
import numpy as np

# Input 12 numbers and add them to lists
input_list1 = []
input_list2 = []
input_list3 = []
print(
        " Du kommer att mata in 12 tal.\n",
        "De första 6 talen kommer att hammna i en lista,\n",
        "de andra 6 i en annan lista\n"
    )
for i in range(12):
    if i < 4:
        input_list1.append(int(input(f"Mata in tal {i+1}: ")))
    elif i >= 4 and i < 8:
        input_list2.append(int(input(f"Mata in tal {i+1}: ")))
    else:
        input_list3.append(int(input(f"Mata in tal {i+1}: ")))

# list no numpy-array
np_array = np.array([input_list1, input_list2, input_list3])

# numpy-array to dataframe
frame = pd.DataFrame(
                    np_array,
                    index=['2017', '2018', '2019'],
                    columns=['Q1', 'Q2', 'Q3', 'Q4']
                    )

# print dataframe
print(frame)
