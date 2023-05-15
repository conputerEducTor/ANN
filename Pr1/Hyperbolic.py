import numpy as np
from matplotlib import pyplot as plt

def hyp(x):
  return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))

# Hyperbolic derivative
def dhyp(x):
  return 1 - hyp(x) * hyp(x)

# Generating data to plot
x_data = np.linspace(-6,6,100)
y_data = hyp(x_data)
dy_data = dhyp(x_data)

# Plotting
plt.plot(x_data, y_data, x_data, dy_data)
plt.title('Hyperbolic Tangent & Derivative')
plt.legend(['f(x)','f\'(x)'])

plt.grid()
plt.show()