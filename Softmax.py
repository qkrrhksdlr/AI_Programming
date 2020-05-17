# 소프트맥스 함수
import numpy as np

def softmax(x, w):
    e = np.exp(w * x)
    out = np.exp(w * x) / e.sum()
    return out

x = [2.0, 1.0, 0.5]
w = np.ones(3)
y = softmax(x, w)

print(y)
print(np.sum(y))

# 매우 큰 숫자가 입력일 경우에는 상수를 빼기
def softmax2(a, b):
    c = np.max(a * b)
    e = np.exp(a * b - c)
    out = np.exp(a * b - c) / e.sum()
    return out

a = [1010, 1000, 990]
b = np.ones(3)
z = softmax2(a, b)

print(z)
print(np.sum(z))