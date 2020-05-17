# 기하에서의 벡터
import numpy as np

a = np.array([[4], [5], [2], [2]])
b = np.array([[4], [0], [2], [0]])
c = np.array([[2], [2], [0], [1]])

cos_ab = (a.T @ b)[0][0] / (np.linalg.norm(a) * np.linalg.norm(b))
cos_bc = (b.T @ c)[0][0] / (np.linalg.norm(b) * np.linalg.norm(c))
cos_ac = (a.T @ c)[0][0] / (np.linalg.norm(a) * np.linalg.norm(c))

print(cos_ab)
print(cos_bc)
print(cos_ac)

# 고유벡터와 고유값
A = np.array([[1, -2], [2, -3]])
w1, v1 = np.linalg.eig(A)

print(w1)
print(v1)

# SVD (Singular Value Decomposition)
M = np.array([[3, -1], [1, 3], [1, 1]])
U, S, VT = np.linalg.svd(M)

print(U)
print(S)
print(VT)