# ----------------------- C -----------------------
# - funció que mostri, per mòbil (ID), clock speed

import pandas as pd

def function1():
    data = pd.read_csv('data.csv')
    filter = (data['id'] == 10) | \
         (data['id'] == 11) | \
         (data['id'] == 12) | \
         (data['id'] == 13) | \
         (data['id'] == 14) | \
         (data['id'] == 15) | \
         (data['id'] == 16) | \
         (data['id'] == 17) | \
         (data['id'] == 18) | \
         (data['id'] == 19)
    datamobiles = data[filter]
    filtro2 = datamobiles.columns.isin(['id', 'clock_speed'])
    selectedcols = datamobiles.columns[filtro2]
    df1 = datamobiles[selectedcols]
    print(df1)
    return df1