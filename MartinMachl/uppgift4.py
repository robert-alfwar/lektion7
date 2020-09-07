# Martin Machl
import pandas as pd
import numpy as np

numbers_1 = []
numbers_2 = []
numbers_3 = []

print("Mata in totalt 12 heltal.")
for num in range(1, 5):
    number = int(input(f"Tal {num}: "))
    numbers_1.append(number)

for num in range(5, 9):
    number = int(input(f"Tal {num}: "))
    numbers_2.append(number)

for num in range(9, 13):
    number = int(input(f"Tal {num}: "))
    numbers_3.append(number)

print()

arr_1 = np.array(numbers_1)
arr_2 = np.array(numbers_2)
arr_3 = np.array(numbers_3)

dataset = pd.DataFrame({"Array 1" : arr_1, "Array 2" : arr_2, "Array 3" : arr_3})

print(dataset)
