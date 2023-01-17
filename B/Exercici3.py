# ----------------------- B -----------------------
# - funció que mostri, per ciutat, la densitat per M2

import pandas as pd
import matplotlib.pyplot as plt


def function3():
    data = pd.read_csv('data.csv')
    data = data.dropna()
    data['Density  M2'] = data['Density  M2'].replace(',', '', regex=True)
    df = pd.DataFrame(data, columns=['City', 'Density  M2'])
    print(df[:10])
    plt.pie(df["Density  M2"], labels=df["City"])
    plt.title("Ejercicio 3")
    plt.show()
if __name__ == "__main__":
    function3()