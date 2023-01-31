# ----------------------- A ----------------------
# - funció que mostri, les morts totals per mes per ciutat (agafar 10 ciutats)

import pandas as pd


def function2(country1, country2, country3, country4, country5, country6, country7, country8, country9, country10):
    data = pd.read_csv('data.csv')
    filter = (data['location'] == country1) | (data['location'] == country2) | (data['location'] == country2) | (
            data['location'] == country3) | (data['location'] == country4) | (data['location'] == country5) | (
                     data['location'] == country6) | (data['location'] == country7) | (data['location'] == country8) | (
                     data['location'] == country9) | (data['location'] == country10)
    datacountrys = data[filter]
    filter2 = datacountrys.columns.isin(['location', 'date','total_deaths'])
    selectedcols = datacountrys.columns[filter2]
    df2 = datacountrys[selectedcols]
    print(df2)
    return df2