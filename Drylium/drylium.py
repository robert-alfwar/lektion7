import pandas as pd 
import numpy as np
a = []
for i in range(0, 4):
    a.append(input("Skriv ett nummer: "))
b = []
for i in range(0, 4):
    b.append(input("Skriv ett nummer: "))
c = []
for i in range(0, 4):
    c.append(input("Skriv ett nummer: "))
d = np.asarray(a)
e = np.asarray(b)
f = np.asarray(c)
dataset = pd.DataFrame(data=[d, e, f])
print(dataset)