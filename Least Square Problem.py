# Least Square Problem (잔차 크기 최소화)
import numpy as np

A = np.array([[1, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 2]])
B = np.array([[2], [2], [3], [4.1]])

Ap_inv = np.linalg.inv(A.T @ A) @ A.T
x = Ap_inv @ B

print(x)

y, resid, rank, s = np.linalg.lstsq(A, B)

print(y)