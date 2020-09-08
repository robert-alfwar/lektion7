import pandas as pd
import numpy as np 

# fyra st listor
list1 = []
list2 = []
list3 = []
list4 = []

print("Following statements will ask you to give values...\n")
#ta in o dela ut i listor
for f in range(4):
    nr = int(input("type a number for list1: "))
    list1.append(nr)

for x in range(4):
    nrr = int(input("type a number for list2: "))
    list2.append(nrr)
        
for xx in range(4):
    nrrr = int(input("type a number for list3: "))
    list3.append(nrrr)


# numpp = np.array([list1] + [list2] + [list3])
# print(numpp)

#skapa numpy-arraylist för list 1,2,3
arr1 = np.array(list1)
# print("numpy-array 1:", arr1)
arr2 = np.array(list2)
# print("numpyarray 1:", arr2)
arr3 = np.array(list3)
# print("numpyarray 3:", arr3)


#konvertera till panda DataFrame samt dela upp i rader och kolumner.
df = pd.DataFrame(data=(arr1,arr2,arr3), index=["2017", "2018", "2019"], columns=["Q1", "Q2,","Q3","Q4"])
print(df)



    