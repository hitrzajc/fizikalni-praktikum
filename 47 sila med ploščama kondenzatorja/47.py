import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp
import array_to_latex as a2l
import pandas as pd 
import csv

r = ufloat(19, 0.2) / 200
d = ufloat(0.0051, 0.01) / 100
g = 9.81
masa = np.array([0.0002, 0.0004, 0.0006, 0.0008, 0.0010, 0.0012, 0.0014, 0.0016])

data = pd.read_csv(r'Tok.csv', delimiter=";")
data = np.array(data)

data = np.hstack(data)

data_brez = []
temp = []

for i in range(len(data)):
    if i > 0 and i % 6 == 0:
        temp = data[(i - 6):i].tolist()
        data_brez.append(temp)
    elif i == len(data) - 1:
        temp = data[(i - 5):].tolist()
        data_brez.append(temp)

data_brez = np.array(data_brez)
sila = masa[:] * g

print(a2l.to_ltx(data_brez, frmt='{:6.4f}', arraytype=('array')))

data_err = np.zeros_like(data_brez)

average_napetost = np.array([np.average(i) for i in data_brez])

err = np.zeros_like(average_napetost)

for i in range(len(average_napetost)):
    data_err[i] = np.abs(data_brez[i] - average_napetost[i])

average_err = np.array([np.average(i) for i in data_err])

meritve = np.array([average_napetost, average_err, sila]).T

print(a2l.to_ltx(meritve, frmt='{:6.4f}', arraytype='array'))

average_napetost = average_napetost ** 2

for i in range(len(average_napetost)):
    average_err[i] = (2* average_err[i] / average_napetost[i]) * average_napetost[i]

def lin_f (x, k, n):
    return k * x + n

koef, _ = curve_fit(lin_f, average_napetost, sila)

e0 = koef * 2 * (d ** 2 / (r ** 2 * np.pi))
e0_teoreticen = (2.998 * 10**8)**2 * (4 * np.pi * 10**-7)
e0_teoreticen = 1 / e0_teoreticen

print("koeficient", koef)
print("električna konstanta", e0)
print(("teoretičen", e0_teoreticen))

d = unp.sqrt(e0_teoreticen * 2 * np.pi * r**2 / 2 / koef[0])
print("debelina", d)

plt.xlabel("U² [V²]")
plt.ylabel("(F [N]")

plt.errorbar(average_napetost, sila, xerr=average_err, fmt='o', linewidth=2, capsize=6, label="Meritve")
plt.plot(average_napetost, lin_f(average_napetost, *koef), label="Fit")


plt.legend()
plt.savefig("graf.pdf")
plt.show()
plt.close()



