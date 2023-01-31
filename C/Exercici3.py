# ----------------------- C -----------------------
# - funció que mostri, per m`bil (ID) la battery power

import pandas as pd

def function3():
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
        filter2 = datamobiles.columns.isin(['id', 'battery_power'])
        selectedcols = datamobiles.columns[filter2]
        df2 = datamobiles[selectedcols]
        print(df2)
        return df2