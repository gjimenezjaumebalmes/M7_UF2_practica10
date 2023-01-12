# ----------------------- B -----------------------
# - funció que mostri, per ciutat, la densitat per KM2

import pandas as pd


def function_2():
    data = pd.read_csv('data.csv')
    df = pd.DataFrame(data, columns=['City', 'Density KM2'])
    print(df[1:11])


function_2()
