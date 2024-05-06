#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:53:40 2024

@author: pmygu2
"""
def Convergence_Plot(variable):
    '''
    

    Parameters
    ----------
    variable : index of the variable of the dataset that we are interested in:
                  - 1-> rest mass density
                  - 2-> Lorentz factor times velocity
                  - 3-> internal specific energy density per unit mass

    Returns
    ------- pyplot friendly data for convergence
    x : array of N=100, 200, 400, 800 in log10.
    y : array of sum(yn-yanalytcal)/N.

    '''
    import numpy as np
    import matplotlib.pyplot as plt
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
    
    if variable==1:
        title=r'$\rho$'
    elif variable==2:
        title= r'$Wv$'
    elif variable==3:
        title=r'$u$'
    
    # data for 100-point grid
    x100= data100[0:101,0]
    y100= data100[0:101,variable]
    xAn1= dataAn[::128,0]
    yAn1= dataAn[::128,variable]
    conv100=np.zeros(len(x100))
    for i in range(len(x100)): 
        conv100[i]=abs(y100[i]-yAn1[i])
    conv100=np.sum(conv100)/100
    
    # data for 200-point grid
    x200= data200[0:201,0]
    y200= data200[0:201,variable]
    xAn2= dataAn[::64,0]
    yAn2= dataAn[::64,variable]
    conv200=np.zeros(len(x200))
    for i in range(len(x200)): 
        conv200[i]=abs(y200[i]-yAn2[i])
    conv200=np.sum(conv200)/200

    #data for 400-point grid
    x400= data400[0:401,0]
    y400= data400[0:401,variable]
    xAn4= dataAn[::32,0]
    yAn4= dataAn[::32,variable]
    conv400=np.zeros(len(x400))
    for i in range(len(x400)): 
        conv400[i]=abs(y400[i]-yAn4[i])
    conv400=np.sum(conv400)/400

    #data for 800-point grid
    x800= data800[0:801,0]
    y800= data800[0:801,variable]
    xAn8= dataAn[::16,0]
    yAn8= dataAn[::16,variable]
    conv800=np.zeros(len(x800))
    for i in range(len(x800)): 
        conv800[i]=abs(y800[i]-yAn8[i])
    conv800=np.sum(conv800)/800

    #slope first-last point
    slope = (np.log10(conv100)-np.log10(conv800))/(np.log10(100)-np.log10(800))
    slope=round(slope,5)
    
    #plot
    x=np.array([np.log10(100),np.log10(200),np.log10(400),np.log10(800)])
    y=np.array([np.log10(conv100),np.log10(conv200),np.log10(conv400),np.log10(conv800)]) 
    
    return x, y, conv100, conv200, conv400, conv800, slope, title