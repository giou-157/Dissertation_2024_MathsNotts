#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:42:25 2024

@author: pmygu2
"""

import numpy as np
import matplotlib.pyplot as plt
directory="/home/pmygu2/Documents/Fourier/osc-pf.log"
data=np.loadtxt(directory)

# data for 100-point grid
x= data[:,0]
y= data[:,1]

plt.axvspan(x[0]/200, x[len(x)-1]/200,facecolor='lightcyan')
plt.plot(x/200,(y[0]-0.00003*np.sin(0.03*x)),'red',linestyle='--')
#plt.title('Oscillations of '+ r'$\rho$')
#plt.plot(x/200,y,'purple')
plt.title(r'$\rho(t_0)-A\sin(\omega t)$, '+ r'$A=3 x 10^{-5}$, '+r'$\omega=0.03$')
plt.xlabel('Time (milliseconds)')
#plt.ylabel('Central density')
plt.xlim(x[0]/200,x[len(x)-1]/200)
plt.savefig('OSCsin.pdf',format='pdf',dpi=600)
plt.show()