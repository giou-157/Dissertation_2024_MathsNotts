#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 01:41:49 2024

@author: pmygu2
"""

import numpy as np
import matplotlib.pyplot as plt
directoryt0="/home/pmygu2/Documents/Tinitial-N800.dat"
datat0=np.loadtxt(directoryt0)
directory100="/home/pmygu2/Documents/shocktube-N100Copy.dat"
data100=np.loadtxt(directory100)
directory200="/home/pmygu2/Documents/shocktube-N200Copy.dat"
data200=np.loadtxt(directory200)
directory400="/home/pmygu2/Documents/shocktube-N400Copy.dat" 
data400=np.loadtxt(directory400)
directory800="/home/pmygu2/Documents/shocktube-N800Copy.dat"
data800=np.loadtxt(directory800)
directoryAn = "/home/pmygu2/Documents/shocktube-N12800Copy.dat"
dataAn = np.loadtxt(directoryAn)

# data for 100-point grid
xt0= datat0[:,0]
yt0= datat0[:,2]
# data for 100-point grid
x100= data100[:,0]
y100= data100[:,2]
# data for 200-point grid
x200= data200[:,0]
y200= data200[:,2]
#data for 400-point grid
x400= data400[:,0]
y400= data400[:,2]
#data for 800-point grid
x800= data800[:,0]
y800= data800[:,2]
# data from highest resodlution (12800)
xAn=dataAn[:,0]
yAn=dataAn[:,2]
plt.grid(True, color='lightcyan')
plt.title('Shocktube: t=0.35')
plt.plot(xt0,yt0,'--',color='royalblue',label='initial state (t=0)')
plt.plot(x100,y100,color='plum',label='N=100')
plt.plot(x200,y200,color='violet',label='N=200')
plt.plot(x400,y400,color='purple',label='N=400')
plt.plot(x100,y100,color='darkmagenta',label='N=800')
plt.plot(xAn,yAn,color='darkturquoise',label='Analytical sol. (N=12800)')
plt.legend(loc='lower left',fontsize='small')
plt.xlabel('Distance r (non-dimentionalised)')
plt.ylabel(r'$Wv$')
plt.savefig('STLF.pdf',format='pdf',dpi=600)
plt.show()