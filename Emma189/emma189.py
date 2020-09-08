import numpy as np
import pandas as pd

numbers = []
for _ in range(1, 13):
    numbers.append(int(input("Enter a number: ")))

arr = np.array(numbers)
newarr = np.array_split(arr, 3)

pan = pd.DataFrame(data=newarr, index=["2020", "2019", "2018"], columns=["Q1", "Q2", "Q3", "Q4"])

print(pan)
