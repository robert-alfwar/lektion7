import numpy as np
import pandas as pd

numbers = list(map(int, input("Enter 12 different numbers, use space between numbers: ").split())) # Tar input från användaren och konverterar det till en lista
arr = np.array(numbers) # konverterar listan numbers till numpy arrays
splitArr = np.split(arr, 3) # splittar en numpy array till tre numpy arrays med fyra tal i varje
df = pd.DataFrame(data=splitArr, index=["row1", "row2", "row3"], columns=["column1", "column2", "column3", "column4"]) # kombinerar numpy arrayer till en dataframe
print(df)

