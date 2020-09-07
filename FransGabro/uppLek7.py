import pandas as pd
import numpy as np

list_1=[]
list_2=[]
list_3=[]

for i in range(1, 13):
    nmbrs = int(input('Enter Number:'))
    if nmbrs <5:
        list_1.append(nmbrs)
    if nmbrs>4 and nmbrs<9:
        list_2.append(nmbrs)
    if nmbrs>8:
        list_3.append(nmbrs)
    
    nmbrs= nmbrs + 1


    arr_1=np.array(list_1) 
    arr_2=np.array(list_2)
    arr_3=np.array(list_3)

sum_arr= [arr_1, arr_2, arr_3]
sum_nump= np.array(sum_arr)

dataset = pd.DataFrame(data=sum_nump,index=['Row1:','Row2:','Row3:'],columns=['Coumn1','Coumn2','Coumn3','Coumn4'])    


print(dataset)