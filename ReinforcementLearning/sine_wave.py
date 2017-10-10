#just some help on how to make a sin wave

import matplotlib.pyplot as plt
import numpy as np


Fs = 100000
f = .75
sample = 100000
x = np.arange(sample)
y = np.sin(1 * np.pi * f * x / Fs) * .5
plt.plot(x, y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()
