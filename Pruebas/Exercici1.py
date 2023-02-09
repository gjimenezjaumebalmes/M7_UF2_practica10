import pandas as pd
import matplotlib.pyplot as plt

def function1():
    data = pd.read_csv('data.csv')
    data = data.dropna()
    # Remove all rows wit NULL values
    data['x'] = data['x'].replace(',', '', regex=True)