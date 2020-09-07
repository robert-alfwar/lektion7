import pandas as pd
import numpy as np

li = []
li2 = []
li3 = []
st = ""

for x in range(12):
    y = input(f'Skriv in vilken siffra du vill ha på plats: {12 - x}, din input: \n')
    st += y

n = 4
inputChar = [st[i:i+n] for i in range(0, len(st), n)]
print(f'\n Detta är vad du har skrivit in för input {inputChar} \n')
li = list(inputChar[0])
li2 = list(inputChar[1])
li3 = list(inputChar[2])

newList = np.array([li, li2, li3])
df = pd.DataFrame(data=newList, index=["2017", "2018", "2019"], columns=["Q1", "Q2", "Q3", "Q4"])
print(df)