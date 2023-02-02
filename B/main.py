# ----------------------- B -----------------------
# - funció que mostri, per ciutat, el total de població.
# - funció que mostri, per ciutat, la densitat per KM2
# - funció que mostri, per ciutat, la densitat per M2
# - funció main la qual truqui a les 3 funcions i mostri, utilitzant matplotlib,
# 1 gràfica circular per cada funció mostrant els resultats. (Cal que la gràfica
# tingui llegenda i cal mostrar el % en cada “quesito”)

import Exercici2
import Exercici1
import Exercici3
import matplotlib.pyplot as plt
import pandas as pd

# Exercici 1
print("Exercici 1")
Exercici1.function1()
# Exercici 2
print("Exercici 2")
print('Imprimimos la grafica 2: ')
Exercici2.function2()
# Exercici 3
print("Exercici 3")
print('Imprimimos la grafica 3: ')
Exercici3.function3()


def grafica():

        print('Imprimimos la grafica 1: ')
        data = pd.read_csv('data.csv')
        data = data.dropna()
        data['Population'] = data['Population'].replace(',', '', regex=True)
        df = pd.DataFrame(data, columns=['City', 'Population']).head(10)
        plt.pie(df["Population"], labels=df["City"])
        plt.title("Ejercicio 1")
        plt.show()

        print('Imprimimos la grafica 2: ')
        data = pd.read_csv('data.csv')
        data = data.dropna()
        data['Density KM2'] = data['Density KM2'].replace(',', '', regex=True)
        df = pd.DataFrame(data, columns=['City', 'Density KM2']).head(10)
        plt.pie(df["Density KM2"], labels=df["City"])
        plt.title("Ejercicio 2")
        plt.show()

        print('Imprimimos la grafica 3: ')
        data = pd.read_csv('data.csv')
        data = data.dropna()
        data['Density  M2'] = data['Density  M2'].replace(',', '', regex=True)
        df = pd.DataFrame(data, columns=['City', 'Density  M2']).head(10)
        plt.pie(df["Density  M2"], labels=df["City"])
        plt.title("Ejercicio 3")
        plt.show()

grafica()