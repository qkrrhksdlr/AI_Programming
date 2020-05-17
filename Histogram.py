# 기술통계
import numpy as np
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)

x = np.random.normal(size=21)
print(x)

bins = np.linspace(-4, 4, 17)
sns.distplot(x, rug=True, kde=False, bins=bins)
plt.xlabel('x')
plt.show()

print('sample mean = {}'.format(np.mean(x)))
print('sample median = {}'.format(np.median(x)))

ns, bin_edges = np.histogram(x, bins=bins)
m_bin = np.argmax(ns)

print('sample mode range = {}~{}'.format(bins[m_bin], bins[m_bin + 1]))
print('sample variance = {}'.format(np.var(x)))
print('sample standard deviation = {}'.format(np.std(x)))
print('sample skewness = {}'.format(sp.stats.skew(x)))
print('sample kurtosis = {}'.format(sp.stats.kurtosis(x)))