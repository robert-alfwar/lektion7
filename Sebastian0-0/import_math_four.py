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


columns = 3

rows = 4

data = []

counter = 1

for i in range(columns):

    array = []

    for j in range(rows):

        array.append(users_input(msg=f'[number: {counter}/{columns*rows}]'))

        counter += 1

    data.append(ny.array(array))

Frame= pd.DataFrame(data=data,
                     index=['2017', '2018', '2019'],
                     columns=['Q1', 'Q2', 'Q3', 'Q4'])
print(Frame)