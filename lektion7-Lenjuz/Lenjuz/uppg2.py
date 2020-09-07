# 1. Skriv ett program som importerar pandas som pd och numpy som np.
# 2. Ta input på tolv stycken tal. Försök att låta användaren förstå vad det är hen matar in.
# 3. Dela upp de inmatade talen i listor
# 4. Konvertera listorna till numpy-arrays
# 5. Kombinera dessa numpy-arrayer till en dataframe.
# 6. Skriv ut dataframen på skärmen.

import pandas as pd
import numpy as np

# list to fill with input
main_list = []

print("Enter the amount of times you've visited the gym per quarter for the last 3 years, \nfor a total of 12 quarters.")
#counts number of times a number has been entered

counter = 0
# for loop to enter 12 inputs using range
for listing in range(1, 13):
    counter += 1
    main_list.append(int(input(f'Enter number of visits for quarter nr: {counter}: ')))
 
 # numpy array into 3 sublists
sublists = np.array_split(main_list, 3)
#print(f'{sublists} is our 3 sublists into arrays with 4 numbers in each.\n')

# pandas.Dataframe and made 3 rows and 4 columns
df = pd.DataFrame(data=sublists, index=["2017", "2018", "2019"], columns=["Q1", "Q2", "Q2", "Q4"])
print(df)




