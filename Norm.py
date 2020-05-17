# 벡터 Norm
import numpy as np

A = (np.arange(9) - 4)
print(A)

A = np.reshape(A, (3, 3))
print(A)

A_norm = np.linalg.norm(A)
print(A_norm)

# 행렬식(Determinant)
B = np.array([[5, 6], [8, 9]])
det_B = np.linalg.det(B)

print(B)
print(det_B)