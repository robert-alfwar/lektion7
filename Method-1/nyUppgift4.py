import numpy as np
import pandas as pd

numbers = list(map(int, input("Enter 12 different numbers, use space between numbers: ").split())) # Tar input från användaren och konverterar det till en lista

print(f"numbers inputed: {numbers}")
arr = np.array(numbers) # konverterar listan numbers till numpy arrays
splitArr = np.split(arr, 3) # splittar en numpy array till tre numpy arrays med fyra tal i varje

years = pd.Series(pd.date_range("2000", periods=3, freq="Y"))

df = pd.DataFrame(data=splitArr, index=[years.dt.year], columns=["Q1", "Q2", "Q3", "Q4"]) # kombinerar numpy arrayer till en dataframe
print(df)