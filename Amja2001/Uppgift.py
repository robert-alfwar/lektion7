import pandas as pd
import numpy as np

while True:
    try:
        var_user_input = list(map(int, input('Ange 12 stycken tal separerat med mellanslag: ').split()))
        if len(var_user_input) != 12:
            continue
        break
    except ValueError:
        print('Ange endast tal!')

# Dela upp listan i par av 4, alltså 3 listor 4 tal
var_columns = 3
var_rows = 4

var_arraylist = []
counter = 0
for c in range(var_columns):
    var_array = []
    for r in range(var_rows):
        var_array.append(var_user_input[counter])
        counter = counter + 1
    var_arraylist.append(var_array)

numpy_one = np.array(var_arraylist[0])
numpy_two = np.array(var_arraylist[1])
numpy_three = np.array(var_arraylist[2])


var_dataframe = pd.DataFrame(data=var_arraylist,
                             index=['1:', '2:', '3:'],
                             columns=['1:', '2:', '3:', '4:'])

print(var_dataframe)