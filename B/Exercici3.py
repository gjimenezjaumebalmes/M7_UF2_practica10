# ----------------------- B -----------------------
# - funció que mostri, per ciutat, la densitat per M2

import pandas as pd


def function3():
    data = pd.read_csv('data.csv')
    data = data.dropna()
    data['Density  M2'] = data['Density  M2'].replace(',', '', regex=True)
    df = pd.DataFrame(data, columns=['City', 'Density  M2'])
    print(df[:10])
    return df[:10]