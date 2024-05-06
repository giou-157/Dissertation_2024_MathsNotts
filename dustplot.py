#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:07:39 2024

@author: pmygu2
"""

import numpy as np
import matplotlib.pyplot as plt
directory="/home/pmygu2/Documents/DustCollapse/dust-N800.log"
data=np.loadtxt(directory)
plt.title('Dust collapse: profiles in time')
x=data[:,0]
y=data[:,1]
plt.plot(x,y,'magenta',linewidth=3,label=r'$\rho$')
y2=data[:,2]
plt.plot(x,y2,'mediumblue',linewidth=3,label='Lorentz factor')
plt.legend()
plt.xlim(0,50)
plt.axvspan(x[0], x[len(x)-1],facecolor='lightcyan')
plt.xlabel('time [ms]')
plt.savefig('DC.pdf',format='pdf',dpi=600)
plt.show()


data_file = 'dust-N800.dat'
with open(data_file, 'r') as file:
    all_data = file.readlines()

time = []
data_temp = []
data = {}
first_instant = True
for line in all_data:
    if line.startswith('#'):
        # if this is not the first time instant, 'data_temp' will contain all
        # the data values you read before
        if first_instant:
            first_instant = False
        else:
            data[t] = data_temp
            data_temp = []
        
        line_split = line.split('=')
        t = line_split[1]
        t = t.strip()            # remove '\n' (new line char)
        time.append(t)
    # if the line is empty (only whitespaces), just skip it
    elif line.isspace():
        pass
    # if it's not empty and it's not a time instant, it's a data line
    else:
        line = line.strip()     # remove '\n'
        line = line.split(' ')  # spaces are used to separate data
        data_line = []
        for Y in line:
            Y = float(Y)        # string -> float
            data_line.append(Y)
        data_temp.append(data_line)

# last time instant
data[t] = data_temp


# HOW DATA ARE SAVED:
#   time    vector of Nt time instants 
#   data    dictionary, where
#               - the keys are the time instants (contained in 'time')
#               - the values are 2D lists representing the solution for each time 
#               instant 

# EXAMPLE
#   t = time[2]                 # 3rd time instant
#   my_results = data[t]        # results for the 3rd time instant
#   my_line = my_results[5, :]  # 6h line of the block of results


# IF YOU WANT TO PRINT THE RESULTS OF EACH TIME INSTANT TO A DIFFERENT FILE
# (whose name is the time instant)
print_to_file = False          # set to True

if print_to_file:
    for t in time:
        results = data[t]
        with open(t, 'w') as file:
            np.savetxt(file, results)

clr=['forestgreen','mediumblue','blueviolet','darkorange','crimson']

for t in time:
    ytot=np.array(data[t])
    x=ytot[:,0]
    y=ytot[:,1]
    
    if t=='30': 
        plt.plot(x,y,color='forestgreen',linewidth=3,label=t+' ms')
    elif t=='40':
        plt.plot(x,y,color='mediumblue',linewidth=3,label=t+' ms')
    elif t=='50':
        plt.plot(x,y,color='magenta',linewidth=3,label=t+' ms') 
        
    
    
plt.legend()
plt.xlim(0,7)
plt.title('Dust collapse: radial profile')
plt.xlabel('r [km]')
plt.ylabel(r'$\rho$')
plt.grid(True, color='paleturquoise')
plt.savefig('DCTSteps.pdf',format='pdf',dpi=600)
plt.show()
