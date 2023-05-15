import numpy as np
from matplotlib import pyplot as plt

# Rectified Linear Unit
def relu(x):
  temp = [max(0,value) for value in x]
  return np.array(temp, dtype=float)
# Derivative for RELU
def drelu(x):
  temp = [1 if value>0 else 0 for value in x]
  return np.array(temp, dtype=float)

# Generating data to plot
x_data = np.linspace(-6,6,100)
y_data = relu(x_data)
dy_data = drelu(x_data)

# Plotting
plt.plot(x_data, y_data, x_data, dy_data)
plt.title('RELU & Derivative')
plt.legend(['f(x)','f\'(x)'])
plt.grid()
plt.show()