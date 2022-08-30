import numpy as np
import matplotlib.pyplot as plt
import sys
a = np.linspace(-10, 10, 100)
b = np.linspace(-10, 10, 100)
a, b = np.meshgrid(a, b)
z = 2*a*b
fig = plt.figure(figsize=[12, 8])
fig.suptitle('og-imaginary: 2*a*b')
ax = plt.axes(projection='3d')
ax.plot_surface(a, b, z)
plt.show()
