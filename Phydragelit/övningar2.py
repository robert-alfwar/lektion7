numbersaver = ''  

for y in range(10):
    for x in range(y):
        numbersaver += f'{y}'
        if(x==(y-1)):
            numbersaver += f'\n'

print(numbersaver)


