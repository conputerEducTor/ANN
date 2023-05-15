import numpy as np
from matplotlib import pyplot as plt

# Sigmoidal
def sig(x):
  return 1/(1+np.exp(-x))

# Sigmoidal derivative
def dsig(x):
  return sig(x) * (1- sig(x))

# Generating data to plot
x_data = np.linspace(-6,6,100)
y_data = sig(x_data)
dy_data = dsig(x_data)

# Plotting
plt.plot(x_data, y_data, x_data, dy_data)
plt.title('Sigmoid Function & Derivative')
plt.legend(['f(x)','f\'(x)'])



plt.grid()
plt.show()
