# 이항부포
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

N = 10
mu = 0.6
rv = sp.stats.binom(N, mu) # rv.pmf 확인
np.random.seed(0)
x = rv.rvs(100) # rvs : 무작위 표본 sampling
print(x)

sns.countplot(x)
plt.title('simulation of binomial distrbution')
plt.xlabel('random value')
plt.show()