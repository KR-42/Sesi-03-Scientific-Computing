# -*- coding: utf-8 -*-
"""Sesi03Interpolasi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iLuNMbIVda1gdJdzX2HS4HYamrflDfLi
"""

from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')

x = [0, 1, 2, 3, 4, 5]
y = [1, 3, 3, 5, 2, 2]

f = interp1d(x,y)

x_lin = np.linspace(0,5,100)
y_lin = f(x_lin)

y_ask = f(3.1)
print (y_ask)

plt.plot(x,y,'ob')
plt.plot(x_lin,y_lin,'b')
plt.plot(3.1,f(3.1),'ro')
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-poster")

# %matplotlib inline
def divided_diff(x, y):
  '''
  function to calculate the divided
  differences table
  '''

  n = len(y)
  coef = np.zeros([n, n])
  #the first collum is y
  coef[:, 0] = y

  for j in range(1, n):
    for i in range(n - j):
      coef[i][j] = \
      (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
  return coef

def newton_poly(coef, x_data, x):
  '''
  evaluate the newton polunomial
  at x
  '''
  n = len(x_data) - 1
  p = coef[n]
  for k in range(1, n+1):
    p = coef[n-k] + (x - x_data[n-k]) * p
  return p

x = np.array([-5, -1, 0, 2])
y = np.array([-2, 6, 1, 3])
# get the divided difference coef
a_s = divided_diff(x, y)[0, :]

# evaluate on new data points
x_new = np.arange(-5, 2.1, .1)
y_new = newton_poly(a_s, x, x_new)

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.plot(x_new, x_new, 'go')
plt.plot(x_new, y_new)

"""# **Cubic Spline Interpolation**"""

x = [0, 1, 2, 3, 4, 5]
y = [1,3, 3, 5, 2, 2]

f = CubicSpline(x, y, bc_type = 'natural')

x_cub = np.linspace(0, 5, 100)
y_cub = f(x_cub)

y_ask = f(2.9)
print (y_ask)

plt.plot(x,y,'ob')
plt.plot(x_cub,y_cub,'b')
plt.plot(2.9, f(2.9), 'ro')
plt.show()

"""# **Quiz singkat**

Olympiade tahun 1990, juara lomba sprint 100 m adalah Ben Johnson. Catatan larinya ketika 0 detik kecepatannya adalah 10 m/sk. Pada saat 5 meter kecepatannya adalah 15 m/s. Pada saat 10 meter kecepatannya adalah 20 m/s. Berapa kecepatan larinya pada jarak 7.2 m?

Jawab dengan python

t0 = 0
t1 = 5 s
t2 = 10 s
v0 = 10 m/s
v1 = 15 m/s
v2 = 20 m/s


"""

import numpy as np
from scipy.interpolate import interp1d

t = [0, 5, 10]
v = [10, 15, 20]

f = interp1d(t, v)

t_ask = 7.2
v_ask = f(t_ask)
print(v_ask)