# 2차원 다변수 함수
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    out = 2*x**2 + 6*x*y + 7*y**2 - 26*x - 54*y + 107
    return out

x = np.linspace(-3, 7, 100)
y = np.linspace(-3, 7, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, linewidth=0.1)
ax.view_init(40, -110)
plt.xlabel('x')
plt.ylabel('y')
ax.set_zlabel('z')
plt.title('surface plot')
plt.show()