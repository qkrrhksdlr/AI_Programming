# Gradient Descent를 이용한 선형회귀
import numpy as np
import matplotlib.pyplot as plt

lr = 0.01 # learning rate
n_iter = 1000 # 반복횟수
X = 2 * np.random.rand(200, 1) # Input data
y = 4 + 3 * X + np.random.randn(200, 1) # Output data
theta = np.random.randn(2, 1) # parameter 0, 1
X_b = np.c_[np.ones((len(X), 1)), X] # Input data with bias

plt.scatter(X, y)
plt.xlabel('X')
plt.ylabel('y')
plt.grid(True)
plt.show()

def cal_cost(theta, X, y):
    m = len(y)
    predictions = X.dot(theta)
    cost = 1 / (2 * m) * np.sum(np.square(predictions - y))
    return cost

def gradient_descent(X, y, theta, learning_rate=0.01, iterations=100):
    m = len(y)
    cost_history = np.zeros(iterations)
    theta_history = np.zeros((iterations, 2))
    for it in range(iterations):
        prediction = np.dot(X, theta)
        theta = theta - (1 / m) * learning_rate * (X.T.dot((prediction - y)))
        theta_history[it, :] = theta.T
        cost_history[it] = cal_cost(theta, X, y)
    return theta, cost_history, theta_history

theta, cost_history, theta_history = gradient_descent(X_b, y, theta, lr, n_iter)

print('Theta0 : {}'.format(theta[0, 0]))
print('Theta1 : {}'.format(theta[1, 0]))
print('Final cost : {}'.format(cost_history[-1]))

plt.scatter(X, y)
plt.plot(X, theta[1, 0] * X + theta[0, 0], 'r--')
plt.xlabel('X')
plt.ylabel('y')
plt.grid(True)
plt.show()

plt.plot(cost_history, 'k--', label='cost')
plt.plot(theta_history[:, 0], 'r--', label='$\\theta_0$')
plt.plot(theta_history[:, 1], 'b--', label='$\\theta_1$')
plt.legend()
plt.xlabel('iteration')
plt.ylabel('cost')
plt.grid(True)
plt.show()