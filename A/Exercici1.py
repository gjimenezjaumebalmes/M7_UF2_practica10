# ----------------------- A ----------------------
# - funció que mostri, per país (agafar 10 països), la quantitat de casos total per mes

import pandas as pd


def function1(country1, country2, country3, country4, country5, country6, country7, country8, country9, country10):
    data = pd.read_csv('data.csv')
    filter = (data['location'] == country1) | \
             (data['location'] == country2) | \
             (data['location'] == country2) | \
             (data['location'] == country3) | \
             (data['location'] == country4) | \
             (data['location'] == country5) | \
             (data['location'] == country6) | \
             (data['location'] == country7) | \
             (data['location'] == country8) | \
             (data['location'] == country9) | \
             (data['location'] == country10)
    datacountrys = data[filter]
    filter2 = datacountrys.columns.isin(['location', 'date', 'total_cases'])
    selectedcols = datacountrys.columns[filter2]
    datacountrys2 = datacountrys[selectedcols]
    separar = datacountrys.date.str.split(pat='-', expand=True)
    datacountrys3 = pd.DataFrame(separar, columns=[1])
    datacountrys4 = pd.DataFrame(datacountrys2, columns=["location", "total_cases"])
    df1 = pd.concat([datacountrys4, datacountrys3], axis=1)
    print(df1)

    return df1

