import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

# Генерируем выборку
x = sts.norm.rvs(0.0,1.0, size=5000)

plt.plot(x)
plt.show()

# Получим теоритические параметры
m,v,s,k = sts.norm.stats(0.0,1.0, moments='mvsk')

print(sts.kstest(x, 'norm',(x.mean(), x.std()), N=5000))