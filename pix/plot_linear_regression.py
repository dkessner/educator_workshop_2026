#!/usr/bin/env python
#
# plot_linear_regression.py
#

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Polynomial

rng = np.random.default_rng(420)

# generate data

data_size = 15 
x = rng.uniform(0, 10, size=data_size)
y = 2 + .5*x + rng.normal(size=data_size)

x_begin = min(x)
x_end = max(x)

# scatter plot

fig, ax = plt.subplots(figsize=(9, 9))
ax.set_ylim(0, 10)
ax.scatter(x, y, s=60, alpha=0.7, edgecolors="k")

plt.savefig("pix/linear_regression_0.jpg")

# line

line = Polynomial.fit(x, y, deg=1)
x_line, y_line = line.linspace(20, [x_begin, x_end])
ax.plot(x_line, y_line, color="b", lw=2.5)

plt.savefig("pix/linear_regression_1.jpg")

# poly

poly = Polynomial.fit(x, y, deg=9)
x_poly, y_poly = poly.linspace(20, [x_begin, x_end])
ax.plot(x_poly, y_poly, color="r", lw=2.5)

plt.savefig("pix/linear_regression_2.jpg")


