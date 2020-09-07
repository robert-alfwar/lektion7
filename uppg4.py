import pandas as pd
import numpy as np

num_list = []
heltal = 0
loop_counts = 0

print("Nu ska du mata in 12st heltal.")
while loop_counts < 12:
    heltal += 1
    loop_counts += 1
    nums = input(f'Mata in heltal {heltal}: ')
    num_list.append(int(nums))
splitted_list1 = np.array(num_list[0:3])
splitted_list2 = np.array(num_list[4:7])
splitted_list3 = np.array(num_list[8:11])

df = pd.DataFrame({"List 1": splitted_list1,
                   "List 2": splitted_list2,
                   "List 3": splitted_list3})
print(df)
