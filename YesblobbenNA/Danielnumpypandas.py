import numpy as np
import pandas as pd

number_array = []
number_array2 = []
number_array3 = []
#Tomma listor

count = 1
#Startvärde

while(count < 13):
    if count < 5:
        user_input = int(input(f'Skriv in lottonummer {count} på rad 1: '))
        number_array.append(user_input)
        pass
    elif count < 9:
        user_input = int(input(f'Skriv in lottonummer {count} på rad 2: '))
        number_array2.append(user_input)
        pass
    else:
        user_input = int(input(f'Skriv in lottonummer {count} på rad 3: '))
        number_array3.append(user_input)
    count = count + 1
#Input från användare adderas till listorna

number_array = np.array(number_array)
number_array2 = np.array(number_array2)
number_array3 = np.array(number_array3)
#Listorna konverteras till arrays

data = {"2019" : number_array, "2018" : number_array2, "2017" : number_array3}
df = pd.DataFrame(data, index = ["Q1", "Q2", "Q3", "Q3"])
print(df)
#Lägger till arrays till en databas
