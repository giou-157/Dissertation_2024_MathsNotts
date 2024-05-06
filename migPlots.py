#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:11:20 2024

@author: pmygu2
"""

import numpy as np
import matplotlib.pyplot as plt
directory="/home/pmygu2/Documents/Migration/mig-pf.dat"
data=np.loadtxt(directory)

directory1="/home/pmygu2/Documents/Migration/mig-pf.log"
data1=np.loadtxt(directory1)

dataaa=data1
x=dataaa[:,0]
y=dataaa[:,1]
# Add labels and legend

plt.xlabel('Time (milliseconds)')
plt.plot(x,y,'magenta')
plt.ylabel(r'$\rho$')  # Change to the appropriate column label
plt.title('Migration stable-unstable branch')
#plt.xlim(0,5)
plt.grid(True,color='lightseagreen')
#plt.savefig('MigInT.pdf',format='pdf',dpi=600)
plt.show()
