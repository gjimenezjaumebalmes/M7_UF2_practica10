# ----------------------- B -----------------------
# - funció que mostri, per ciutat, la densitat per M2

import pandas as pd


def function_3():
    data = pd.read_csv('data.csv')
    df = pd.DataFrame(data, columns=['City', 'Density  M2'])
    print(df[1:11])


function_3()
