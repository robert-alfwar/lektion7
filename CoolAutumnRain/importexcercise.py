import pandas as pd
import numpy as np

user_list = list()
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
years = [2017, 2018, 2019]

def input_value(year):
    for quarter in quarters:
        user_list.append(int(input(f'Fyll i resultat för {quarter} år {year}.\n: ')))
    return user_list

a = np.array(input_value(2017)[0:4])
b = np.array(input_value(2018)[4:8])
c = np.array(input_value(2019)[8:12])

df = pd.DataFrame([a, b, c], index=years, columns=quarters)
print(df)
