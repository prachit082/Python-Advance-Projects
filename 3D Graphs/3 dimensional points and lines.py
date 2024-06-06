import numpy as np # type: ignore
import matplotlib.colors as col # type: ignore
from mpl_toolkits.mplot3d import Axes3D # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Data for a three-dimensional line
z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)

# Create a 3D axes object
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, color='grey')  # Plot the three-dimensional line

# Data for three-dimensional scattered points
z = 15 * np.random.random(100)
x = np.sin(z) + 0.1 * np.random.randn(100)
y = np.cos(z) + 0.1 * np.random.randn(100)

ax.scatter(x, y, z, c=z, cmap='Greens')  # Plot the three-dimensional scattered points

plt.show()