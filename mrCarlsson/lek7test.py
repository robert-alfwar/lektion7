import numpy as np
import pandas as pd
arr=[]
n=12
for _ in range(n): 
    arr.append(int(input("tal :")))
a = np.array([[arr[0:4]],[arr[4:8]], [arr[8:12]]])
data = { 'Numbers 1.':[a[0]], 'Numbers 2.':[a[1]], 'Numbers 3.' :[a[2]]}

  
# Creates pandas DataFrame. 
df = pd.DataFrame(data) 
  
# print the data 
print(df)