import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig=plt.figure()
ax=Axes3D(fig)
x=np.linspace(-10,10,300)
y=np.linspace(-10,10,300)
x,y=np.meshgrid(x,y)

def z(x,y):
    return ((np.sqrt(np.abs(x))))
ax.plot_surface(x,y,z(x,y))

def z(x,y):
    return ((-np.sqrt(np.abs(x))))
ax.plot_surface(x,y,z(x,y))


plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

plt.show()
