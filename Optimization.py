# 최대경사법
import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return (x - 2)** 2 + 2

def f1d(x):
    """f1(x)의 도함수"""
    return 2 * (x - 2.0)

xx = np.linspace(-1, 4, 100)
plt.plot(xx, f1(xx), 'k-')

# step size
mu = 0.4

# k = 0
x = 0 # 시작위치
plt.plot(x, f1(x), 'go', markersize=10)
plt.text(x + 0.1, f1(x) + 0.1, '1st trial')
plt.plot(xx, f1d(x) * (xx - x) + f1(x), 'b--')
print('1st trial : x_1 = {:.2f}, g_1 = {:.2f}'.format(x, f1d(x)))

# k = 1
x = x - mu * f1d(x)
plt.plot(x, f1(x), 'go', markersize=10)
plt.text(x - 0.2, f1(x) + 0.4, '2nd trial')
plt.plot(xx, f1d(x) * (xx - x) + f1(x), 'b--')
print('2nd trial : x_2 = {:.2f}, g_2 = {:.2f}'.format(x, f1d(x)))

# k = 2
x = x - mu * f1d(x)
plt.plot(x, f1(x), 'go', markersize=10)
plt.text(x - 0.2, f1(x) - 0.7, '3rd trial')
plt.plot(xx, f1d(x) * (xx - x) + f1(x), 'b--')
print('3rd trial : x_3 = {:.2f}, g_3 = {:.2f}'.format(x, f1d(x)))

plt.xlabel('x')
plt.ylabel('$f_1(x)$')
plt.title('optimization by using steepest gradient descent')
plt.ylim(0, 10)
plt.grid(True)
plt.show()