# ----------------------- B -----------------------
# - funció que mostri, per ciutat, la densitat per KM2

import pandas as pd


def function2():
    data = pd.read_csv('data.csv')
    data = data.dropna()
    data['Density KM2'] = data['Density KM2'].replace(',', '', regex=True)
    df = pd.DataFrame(data, columns=['City', 'Density KM2'])
    print(df[:10])
    return df[:10]