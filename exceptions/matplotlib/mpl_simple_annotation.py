import matplotlib.pyplot as plt # so we don't have to look at mpl's backend
import numpy as np

import plotly.plotly as py
py.sign_in('TestBot', 'r1neazxo9w')

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.ylim(-2,2)
fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='mpl-simple-annotation')
