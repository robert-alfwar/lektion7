import pandas as pd
import numpy as np

li = []
li2 = []
li3 = []
st = ""

for x in range(12):
    y = input(f"Skriv in {12 - x}")
    st += y

n = 4
inputChar = [st[i:i+n] for i in range(0, len(st), n)]

li = list(inputChar[0])
li2 = list(inputChar[1])
li3 = list(inputChar[2])

newList = np.array([li, li2, li3])
df = pd.DataFrame(data=newList)
print(df)