# 로그정규분포
import scipy as sp
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
mu = 1
s = 0.5
rv1 = sp.stats.norm(loc=mu)
x1 = rv1.rvs(1000)
x2 = np.exp(s * x1)

fig, ax = plt.subplots(1, 2)
sns.distplot(x1, kde=False, ax=ax[0], fit=sp.stats.norm)
ax[0].set_title('normal distribution')
sns.distplot(x2, kde=False, ax=ax[1], fit=sp.stats.lognorm)
ax[1].set_title('log_normal distribution')
plt.tight_layout()
plt.show()