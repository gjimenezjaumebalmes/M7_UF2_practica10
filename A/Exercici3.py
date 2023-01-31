# ----------------------- A ----------------------
# - funció que mostri la “reproduction_rate “ per mes per pais (agafar 10 països)

import pandas as pd


def function3(country1, country2, country3, country4, country5, country6, country7, country8, country9, country10):
    data = pd.read_csv('data.csv')
    filter = (data['location'] == country1) | (data['location'] == country2) | (data['location'] == country2) | (
            data['location'] == country3) | (data['location'] == country4) | (data['location'] == country5) | (
                     data['location'] == country6) | (data['location'] == country7) | (data['location'] == country8) | (
                     data['location'] == country9) | (data['location'] == country10)
    datacountrys = data[filter]
    filtro2 = datacountrys.columns.isin(['location', 'date', 'reproduction_rate'])
    selectedcols = datacountrys.columns[filtro2]
    df3 = datacountrys[selectedcols]
    print(df3)
    return df3
