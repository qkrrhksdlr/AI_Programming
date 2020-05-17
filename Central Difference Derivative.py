# 단순 미분
import numpy as np
import matplotlib.pylab as plt

def derivative(f, a, method='central', h=1e-4):
    if method == 'central':
        return (f(a + h) - f(a-h))/(2*h)
    elif method == 'forward':
        return (f(a + h) - f(a))/h
    elif method == 'backward':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method must be 'central','forward' or 'backward'.")

x = np.linspace(0, 5*np.pi, 100)
y = np.sin(x)
dydx = derivative(np.sin, x)

plt.plot(x, y, 'b', label='y = sin(x)')
plt.plot(x, dydx, 'r.', label='Central Difference of y')
plt.title('Central Difference Derivative of y = sin(x)')
plt.legend(loc='best')
plt.grid()
plt.show()