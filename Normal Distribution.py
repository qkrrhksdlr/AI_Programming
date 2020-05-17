# 정규분포
import scipy as sp
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mu = 0
std = 1
rv = sp.stats.norm(mu, std)
np.random.seed(0)
X = rv.rvs(20)
print(X)

sns.distplot(X, rug=True, kde=False, fit=sp.stats.norm)
plt.title('simulation of normal distrbution')
plt.xlabel('random value')
plt.ylabel('probabilitiy')
plt.show()