import pandas as pd
import numpy as ny


def users_input(msg: str = '', prompt: str = ':', retries: int = 3) -> str:
    #Gets users input
    try:
        value = input(f'{msg} {prompt} ')
        return value
    except ValueError:
        if retries:
            return users_input(msg=msg, promt=prompt, retries=retries-1)
        else:
            raise


COLS = 3
ROWS = 4

data = []
counter = 1
for i in range(COLS):
    array = []
    for j in range(ROWS):
        array.append(users_input(msg=f'[number: {counter}/{COLS*ROWS}]'))
        counter += 1
    data.append(ny.array(array))

Box = pd.Databox(data=data,
                     index=['2017', '2018', '2019'],
                     columns=['1', '2', '3', '4'])
print(box)