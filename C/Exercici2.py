# ----------------------- C -----------------------
# - funció que mostri, per mòbil (ID), els megapixels que tenen.

import pandas as pd
import matplotlib.pyplot as plt

def function2():
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
    filter2 = datamobiles.columns.isin(['id', 'fc'])
    selectedcols = datamobiles.columns[filter2]
    df3 = datamobiles[selectedcols]
    print(df3)
    return df3