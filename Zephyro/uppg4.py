# Uppgift 4
# Author: Zephyro Kemstedt

# 4.1

# Skriv ett program som låter användaren mata in 12 tal. Gör dessa till
# tre numpy arrays med fyra tal i varje, sätter samman dessa till en pandas
# dataframe och slutligen skriver ut dataframen.

# Specifikation:
# 1. Skriv ett program som importerar pandas som pd och numpy som np.
# 2. Ta input på tolv stycken tal. Försök att låta användaren förstå
#    vad det är hen matar in.
# 3. Dela upp de inmatade talen i listor
# 4. Konvertera listorna till numpy-arrays
# 5. Kombinera dessa numpy-arrayer till en dataframe.
# 6. Skriv ut dataframen på skärmen.


import pandas as pd
import numpy as np


def get_user_input(msg: str = '', prompt: str = '>>', retries: int = 3) -> str:
    """Helper function to get user input"""
    try:
        value = input(f'{msg} {prompt} ')
        return value
    except ValueError:
        if retries:
            return get_user_input(msg=msg, promt=prompt, retries=retries-1)
        else:
            raise


COLS = 3
ROWS = 4

data = []
counter = 1
for i in range(COLS):
    array = []
    for j in range(ROWS):
        array.append(get_user_input(msg=f'[{counter}/{COLS*ROWS}]'))
        counter += 1
    data.append(np.array(array))

frame = pd.DataFrame(data=data,
                     index=['2017', '2018', '2019'],
                     columns=['Q1', 'Q2', 'Q3', 'Q4'])
print(frame)


# 4.2

#   4.2.1. Lägg upp din kod från förra övningen i github.
#   https://github.com/robert-alfwar/lektion7/tree/zephyro

#   4.2.2. Hitta någon annans upplagda kod
#   https://github.com/robert-alfwar/lektion7/tree/nisserino

#       4.2.3. Modifiera den koden så att:

#       3a Pandas skriver ut årtalen 2017-2019 som rubrik för varje array
#       https://github.com/robert-alfwar/lektion7/pull/2/commits/d82ab7507d8a5f3923cf08163b96ffe091e56998

#       3b Pandas skriver ut Q1, Q2, Q3 och Q4 som rubrik för varje element
#       i arrayerna
#       https://github.com/robert-alfwar/lektion7/pull/2/commits/d82ab7507d8a5f3923cf08163b96ffe091e56998

#       3c Användaren vid inmatning får information om vad hen skriver in.
#       https://github.com/robert-alfwar/lektion7/pull/2/commits/055cf967a3d687d7166be0270f97d4a64cb9c6fc


# 4.3. Utförande
# https://github.com/robert-alfwar/lektion7/pull/1


# 4.4. Kommentarer
# https://github.com/robert-alfwar/lektion7/pull/1/files#r484447200
