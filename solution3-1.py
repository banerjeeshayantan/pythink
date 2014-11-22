
#1: Eigenvalues of a random matrix
#Take a large-dimensional (dimension 100, 1000, or more) square random
#matrix whose elements are independently drawn from N (0; 1) and plot a
#histogram of its eigenvalues to illustrate Wigner’s semicircle law (see
#en.wikipedia.org/wiki/Wigner_semicircle_distribution).

import numpy as np
from scipy import linalg as LA
from random import gauss
from math import sqrt
import matplotlib.pylab as plt


n = 1000                        # dimension of the random matrix
x = np.zeros((n,n))             # initialize a two-dimensional array
for i in range(n):
    for j in range(i,n):
        x[i, j] = gauss(0,1)    # random element
        x[j, i] = x[i, j]       # symmetrically placed element
evals = LA.eigvals(x).real      # compute eigenvalues and take their real part (imaginary is zero anyway because x is symmetric)

bins, vals, patches = plt.hist(evals.real, bins = 50)   # draw the histogram of all eigenvalues
H = max(bins)                                           # height of the circle
R = max(abs(vals))                                      # radius of the circle
x = np.linspace(-R,R,100)                               # an x-grid to draw the semicircle
y = np.array([H*sqrt(1-(xval/R)**2) for xval in x])     # y-values for the semicircle

plt.xlim(-70,70)                                        # a bit of margin on the sides
plt.ylim(0,30)                                          # a bit of margin at the top
plt.plot(x, y, color = 'r', linewidth = 3)              # plot the semicircle
plt.xlabel(r'$\lambda$', fontsize = 18)                 # label x-axis
plt.ylabel(r'$n$', fontsize = 18)                       # label y-axis
plt.axes().set_aspect(R/H)                              # aspect ratio 1:1 (so that our distribution looks like a circle)
plt.savefig('wigner.pdf')                               # save the output
plt.show()
