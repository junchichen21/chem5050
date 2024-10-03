import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

data = pd.read_csv('trouton.csv')

kcal_to_J = 4184

data['H_v (J/mol)'] = data['H_v (kcal/mol)'] * kcal_to_J

sns.scatterplot(data=data, x='T_B (K)', y='H_v (J/mol)', hue='Class', palette='Set1')

def ols_slope(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    return numerator / denominator

def ols_intercept(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    slope = ols_slope(x, y)
    return y_mean - slope * x_mean

def ols(x, y):
    slope = ols_slope(x, y)
    intercept = ols_intercept(x, y)
    return slope, intercept

slope, intercept = ols(data['T_B (K)'], data['H_v (J/mol)'])

x = np.linspace(0, 2600)

predict_H_v = slope * x + intercept

plt.plot(x, predict_H_v, color='black', linestyle='--')

ols_equ = rf"$H_v$ = {slope:.2f} J/(mol*K) * $T_B$ + {intercept/1000:.4f} kJ/mol"

plt.text(800, 50000, s=ols_equ)

plt.title('Trouton’s Rule')

plt.show()
