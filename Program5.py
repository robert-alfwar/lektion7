import pandas as pd
import numpy as np

numbers_list = []
counter = 0

print("Ange totalt 12st heltal.")

#repeats input prompt and lets user know how many inputs are made
while counter < 12:
    counter += 1
    numbers_list.append(int(input(f'Heltal nummer {counter}: ')))

#creates new lists based on index
split_list_1 = numbers_list[0:4]
split_list_2 = numbers_list[4:8]
split_list_3 = numbers_list[8:12]

#creates new numpy.arrays based on the split_lists
np_array_1 = np.array(split_list_1)
np_array_2 = np.array(split_list_2)
np_array_3 = np.array(split_list_3)

#nested the array list and converted to numpyarray
np_set = [np_array_1,np_array_2,np_array_3]
np_col = np.array(np_set)
#adds the np.arrays to a pd.DataFrame
dataframe = pd.DataFrame(data=np_col,index=['2017:','2018:','2019:'],columns=['Q1','Q2','Q3','Q4'])

print(dataframe)
#Outputs, ex:
#   List 1  List 2  List 3
#0       1       5       9
#1       2       6      10
#2       3       7      11
#3       4       8      12