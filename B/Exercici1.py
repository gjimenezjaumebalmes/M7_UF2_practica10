# ----------------------- B -----------------------
# - funció que mostri, per ciutat, el total de població.

import pandas as pd
import matplotlib.pyplot as plt


def function1():
    data = pd.read_csv('data.csv')
    data = data.dropna()
    data['Population'] = data['Population'].replace(',', '', regex=True)
    df = pd.DataFrame(data, columns=['City', 'Population'])
    print(df[:10])
    plt.pie(df["Population"], labels=df["City"])
    plt.title("Ejercicio 1")
    plt.show()
if __name__ == "__main__":
    function1()
