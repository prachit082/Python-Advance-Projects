import numpy as np # type: ignore
import matplotlib.colors as col # type: ignore
from mpl_toolkits.mplot3d import Axes3D # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Define x, y, z
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(x, y, z, color='black')
ax.set_title('wireframe')
plt.show()