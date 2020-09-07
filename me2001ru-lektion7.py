import pandas as pd
import numpy as np

userData = [int(x) for x in input("Enter your 12 values: ").split()]
list1 = userData[:4]
list2 = userData[4:8]
list3 = userData[8:]

x = np.array(list1)
y = np.array(list2)
z = np.array(list3)

mydf = pd.DataFrame([list1, list2, list3], columns = ["a", "b", "c", "d"])

print(mydf)