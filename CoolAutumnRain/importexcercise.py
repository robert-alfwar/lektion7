import pandas as pd
import numpy as np
user_list = input('''
Mata in 4x3 tal (12 totalt, alla whitespace som delimiter): ''').split()
a = np.array(user_list[0:4])
b = np.array(user_list[4:8])
c = np.array(user_list[8:12])
df = pd.DataFrame([a, b, c], columns=['Col1', 'Col2', 'Col3', 'Col4'])
print(df)
