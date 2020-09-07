import pandas as pd
import numpy as np

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
years = [2017, 2018, 2019]

def input_value(year):
    user_list = []
    for quarter in quarters:
        user_list.append(int(input(f'Fyll i resultat för {quarter} år {year}.\n: ')))
    return user_list

df = pd.DataFrame([input_value(year) for year in years], index=years, columns=quarters)
print(df)
