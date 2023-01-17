# ----------------------- B -----------------------
# - funció que mostri, per ciutat, la densitat per KM2

import pandas as pd
import matplotlib.pyplot as plt


def function2():
    data = pd.read_csv('data.csv')
    data = data.dropna()
    data['Density KM2'] = data['Density KM2'].replace(',', '', regex=True)
    df = pd.DataFrame(data, columns=['City', 'Density KM2'])
    print(df[:10])
    plt.pie(df["Density KM2"], labels=df["City"])
    plt.title("Ejercicio 2")
    plt.show()
