#Exothermic reaction releasing heat 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import exp


F, V, C_A, k = 20., 100., 5., 0.15                              # parameters (the same as before)
DH, E_a, c_p, rho, R, T_in = 590, 5000, 1, 1, 8.314, 288        # additional parameters
C0, T0 = 0.5, 288                                               # initial conditions

def RHS((C,T), t):
    dC_over_dt = F * (C_A - C) / V - k * exp(-E_a/(R*T)) * C **2
    dT_over_dt = F * (T_in - T) / V + k * exp(-E_a/(R*T)) * DH * C**2 / (rho * c_p)
    return dC_over_dt, dT_over_dt

t  = np.linspace(0, 20., 51)            # create the time grid
sol = odeint(RHS, (C0,T0), t)           # integrate the set of ODEs

fig = plt.figure()                      # initialize the figure object
ax1 = fig.add_subplot(211)              # create the concentration subplot
ax1.plot(t, sol[:,0])                   # plot the evolution of concentration
ax1.set_xlabel('time [minutes]')        # set the x label
ax1.set_ylabel('concentration [mol/L]') # set the y label
ax1.grid('on')                          # turn on a nice grid (good for number reading)

ax2 = plt.subplot(212)                  # create the temperature subplot
plt.plot(t, sol[:,1])                   # plot the evolution of temperature
ax2.set_xlabel('time [minutes]')        # set the x label
ax2.set_ylabel('temperature [K]')       # set the y label
ax2.set_yticks([200,600,1000,1400,1800,2200])   # change the automatically chosen positions of ticks
ax2.grid('on')                          # turn on a nice grid (good for number reading)

plt.tight_layout()                      # to better separate the subplots
plt.savefig('2D_ODE.pdf')               # save the result
plt.show()                              # show the result
