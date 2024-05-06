# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:13:01 2024

@author: pmygu2
"""

import numpy as np
import matplotlib.pyplot as plt

# read data
data = np.loadtxt('spectrum.txt')
f = data[:, 0]
A = data[:, 1]

plt.figure()
plt.semilogy(f, A, color="magenta")
plt.xlim(25, 6000)
plt.ylim(1e-4, 10)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [-]')
plt.grid(True,color='powderblue')
plt.savefig('spectrum.pdf',format='pdf',dpi=600)
plt.show()

f_max = [1000, 2000, 2800, 3500]
f_min = [0, 1000, 2000, 2800]
for i in range(4):
    f_bin = np.where(f < f_max[i], f, 0)
    f_bin = np.where(f_bin > f_min[i], f_bin, 0)
    A_bin = np.where(f_bin != 0, A, 0)
    idx_max = np.argmax(A_bin)
    f_peak = f_bin[idx_max]
    print(f'Peak: {f_peak:4.0f} Hz')
