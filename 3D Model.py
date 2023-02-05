import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

# Generate data for the plot
X = np.random.rand(100)
Y = np.random.rand(100)
Z = np.random.rand(100)

# Plot the data
ax.scatter(X, Y, Z, marker='+', s=40)


# Add labels to the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
