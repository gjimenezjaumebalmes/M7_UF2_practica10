# ----------------------- B -----------------------
# - funció que mostri, per ciutat, el total de població.

import pandas as pd


def function1():
    data = pd.read_csv('data.csv')
    data = data.dropna()
    data['Population'] = data['Population'].replace(',', '', regex=True)
    df = pd.DataFrame(data, columns=['City', 'Population'])
    print(df[:10])
    return df[:10]