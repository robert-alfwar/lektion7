
import numpy as np
import pandas as pd

numb_list = []
numb_list2 = []
numb_list3 = []

for i in range(4):
    numb1 = input("Skriv in siffra: ")
    numb_list.append(numb1)
    numb2 = input("Skriv in siffra: ")
    numb_list2.append(numb2)
    numb3 = input("Skriv in siffra: ")
    numb_list3.append(numb3)

data = {'Ett':numb_list, 'Två':numb_list2, 'Tre':numb_list3,}
np.array(data)
df = pd.DataFrame(data, columns=['Ett', 'Två', 'Tre'])

print(df)