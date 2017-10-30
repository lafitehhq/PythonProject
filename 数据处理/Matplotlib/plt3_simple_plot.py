# -*- coding: utf-8 -*-

""" 
@File: plt3_simple_plot.py 
@Version:
@Description:
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x + 1
# y = x**2
plt.plot(x, y)
plt.show()