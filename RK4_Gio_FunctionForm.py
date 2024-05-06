# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:46:50 2023

@author: usaig
"""

import numpy as np
import scipy.integrate as scint
import matplotlib.pyplot as plt



def TOV_solver(r_0,r_n,K,rho_c,gamma,rho_c_itv_s,rho_c_itv_e):
    """
    - r_0=initial radius for integration
    - r_n=final radius for integration
    - K,rho_c,gamma= parameter for press
    - rho_c_itv_s, rho_c_itv_e= interval of rho_c for massVSradius plot
    """
    def runge_kutta_4th_order(f, g, y0, r_0, r_n, dr): 
        r_values = np.arange(r_0, r_n + dr, dr)
        num_steps = len(r_values)
        y_values = np.zeros((num_steps, len(y0)))
        y_values[0] = y0

        for i in range(1, num_steps): 
            r = r_values[i - 1]
            y = y_values[i - 1]
        
        
            if r==r_0:                         #if r==r_0  #i<O: 
                k1 = dr * f(r, y) 
                k2 = dr * f(r + 0.5 * dr, y + 0.5 * k1) 
                k3 = dr * f(r + 0.5 * dr, y + 0.5 * k2) 
                k4 = dr * f(r + dr, y + k3)

            else:
                k1 = dr * g(r, y) 
                k2 = dr * g(r + 0.5 * dr, y + 0.5 * k1) 
                k3 = dr * g(r + 0.5 * dr, y + 0.5 * k2) 
                k4 = dr * g(r + dr, y + k3)
            
            y_values[i] = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0
            if y_values[i,1]< 1e-5: 
                y_values[i,1]=0
        return r_values, y_values

       # Define your system of ODEs as a function f(t, y), where y is a vector.
       # System at origin
    def f(r, y):
        m=y[0]
        p=y[1]
        if p< 1e-5: 
            p=0
        K=1
        gamma=2
        rho=(p/K)**(1/gamma)+(p/(gamma-1))
        dm_dr = 4*np.pi*(r**2)*rho
        dp_dr = -((rho+p)*(4*np.pi*rho*(r/3)+4*np.pi*r*p))/(1-8*rho*np.pi*((r**2)/3))
        return np.array([dm_dr, dp_dr])
      # System outside origin
    def g(r, y): 
        m=y[0]
        p=y[1]
        if p<1e-5: 
            p=0
        K=1
        gamma=2
        rho=(p/K)**(1/gamma)+(p/(gamma-1))
        dm_dr = 4*np.pi*(r**2)*rho
        dp_dr = -((rho+p)*(m+4*np.pi*(r**3)*p))/(r*(r-2*m)) 
        return np.array([dm_dr, dp_dr])


    # Set initial conditions, time span, and step size
    n=10000
    dr=(r_n-r_0)/n                          #0.004            #=(r_n-r_0)/n
    m_0=0
    p_0=K*rho_c**gamma
    initial_conditions = np.array([m_0, p_0])

    # Apply the Runge-Kutta method
    r_values, y_values = runge_kutta_4th_order(f,g, initial_conditions, r_0, r_n, dr)
    m=y_values[:, 0]
    p= y_values[:, 1]
    M=m[len(m)-1]

    #find radius of star by finding where pressure is zero
    zero_p = np.where(p==0)[0]
    end=zero_p[0]
    R=r_values[end]
    p=p[0:end]
    m=m[0:end]
    r_values=r_values[0:end]
    print('radius is',R)
    print('total mass is', M)

    #M/R plot:
    rho_c_vec= np.linspace(rho_c_itv_s,rho_c_itv_e,500)    
    M_vec=np.zeros(len(rho_c_vec))
    R_vec=np.zeros(len(rho_c_vec))
    for i in range(len(rho_c_vec)):
        m_0_MR=0
        p_0_MR=K*rho_c_vec[i]**gamma 
        initial_conditions_MR = np.array([m_0_MR, p_0_MR]) 
        r_MR, y_MR = runge_kutta_4th_order(f,g, initial_conditions_MR, r_0, r_n, dr)
        m_MR=y_MR[:, 0]
        p_MR= y_MR[:, 1]
        zero_pMR = np.where(p_MR==0)[0]
        end=zero_pMR[0]
        R_vec[i]=r_MR[end-1]
        M_vec[i]=m_MR[end-1]

    return [R,M,r_values,p,m,M_vec,R_vec,rho_c_vec]



TOV_sol=TOV_solver(0,12,1,0.42,2,0.01,1.8)
plt.plot(TOV_sol[2],TOV_sol[4], 'black', label='mass')
plt.plot(TOV_sol[2],TOV_sol[3], 'dimgray', label='pressure')
plt.xlabel('Radius')
plt.ylabel('Solution values')
plt.legend()
plt.show()

plt.plot(TOV_sol[6],TOV_sol[5],'black')
plt.xlabel('Radius')
plt.ylabel('Mass')
plt.show()
plt.plot(TOV_sol[7],TOV_sol[5],'black')
plt.xlabel(r'$\rho_c$')
plt.ylabel('Mass')
plt.show()
    

