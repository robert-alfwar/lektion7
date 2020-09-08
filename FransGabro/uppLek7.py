import pandas as pd
import numpy as np

list_1=[]
list_2=[]
list_3=[]

for i in range(1, 13):
    nmbrs = int(input('Enter numbers for years 2017-2019, four separate inputs for each year (quarterly):'))
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

sum_arr = [arr_1, arr_2, arr_3]
sum_nump = np.array(sum_arr)

dataset = pd.DataFrame(data=sum_nump,index=['2017:','2018:','2019:'],columns=['Q1','Q2','Q3','Q4'])    


print(dataset)