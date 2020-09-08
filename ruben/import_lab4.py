import pandas as pd
import numpy as np

nums1 = []
nums2 = []
nums3 = []
nums_list = [nums1, nums2, nums3]
y = ["2017","2018","2019"]
q = ["Q1", "Q2", "Q3", "Q4"]
q_index = 0
y_index = 0

print()
print("Three year economic overview for Ruben Inc.") # added header

def business_cycle(nums_list, q, y, q_index, y_index):
    print("\nProvide company revenue in millions of USD.")
    for item in nums_list:
        for _ in range(4): # removed unused variable
            num = int(input(f"Input revenue for {q[q_index]} {y[y_index]}: "))
            item.append(num)
            q_index += 1
        q_index = 0
        y_index += 1
    return nums_list

nums_list = business_cycle(nums_list, q, y, q_index, y_index)

np_arr1 = np.array(nums_list[0])
np_arr2 = np.array(nums_list[1])
np_arr3 = np.array(nums_list[2])

dataset = pd.DataFrame({y[0] : np_arr1, y[1] : np_arr2, y[2] : np_arr3}, 
    index=[q[0], q[1], q[2], q[3]])
print(f'\n{dataset}')