from numpy import random
from simulation import Simulation
import matplotlib.pyplot as plt
import seaborn as sns

x = []
r = Simulation()

for i in range(100):
    x.append(r.get_rate())

sns.distplot(x, hist=False)
plt.show()