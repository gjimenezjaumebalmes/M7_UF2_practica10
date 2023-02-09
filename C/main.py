# ----------------------- C -----------------------
# 1 funció que mostri, per mòbil (ID), clock speed
# 1 funció que mostri, per mòbil (ID), els megapixels que tenen.
# 1 funció que mostri, per m`bil (ID) la battery power
# 1 funció main la qual truqui a les 3 funcions i mostri, utilitzant matplotlib, 1 gràfica barres per cada funció mostrant els resultats. (Cal que la gràfica tingui llegenda)
import matplotlib.pyplot as plt
import pandas as pd
import Exercici2
import Exercici1
import Exercici3


# Exercici 1
print("Exercici 1")
print("----------Clock-Speed---------------")
Exercici1.function1()
# Exercici 2
print("Exercici 2")
print("----------Mega Pixels----------------")
Exercici2.function2()
# Exercici 3
print("Exercici 3")
print("----------Battery Power--------------")
Exercici3.function3()

def grafica():

    colors = ["red", "blue", "green", "yellow", "brown", "purple", "orange", "pink", "grey","black"]
    print("--------Clock Speed------------")
    df = Exercici1.function1()
    nombres = pd.DataFrame(df)
    filterMobile = nombres.pop("id")
    filterValores = nombres.pop("clock_speed")
    array = filterMobile.to_numpy()
    cast = []
    for i in array:
        cast += [str(i)]
    plt.xlabel("ID")
    plt.ylabel("Clock Speed")
    plt.bar(cast, filterValores, width=0.4 , color=colors)
    plt.title("Clock Speed")
    plt.legend(loc="upper left")
    plt.show()


    print("--------MegaPixels------------")
    df2 = Exercici2.function2()
    nombres2 = pd.DataFrame(df2)
    filterValores2 = nombres2.pop("fc")
    fig = plt.figure(figsize = (10, 5))
    plt.xlabel("ID")
    plt.ylabel("Mega Pixels")
    plt.bar(cast, filterValores2, width=0.4, color=colors)
    plt.title("Mega Pixels")
    plt.legend(loc='upper left')
    plt.show()

    print("--------battery_power------------")
    df3 = Exercici3.function3()
    nombres3 = pd.DataFrame(df3)
    filterValores3 = nombres3.pop("battery_power")
    plt.xlabel("ID")
    plt.ylabel("battery power")
    plt.bar(cast, filterValores3, width=0.4 ,color=colors)
    plt.title("Battery Power")
    plt.legend(loc='upper left')
    plt.show()

grafica()