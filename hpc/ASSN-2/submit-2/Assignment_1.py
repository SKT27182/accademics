# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 23:07:09 2022

@author: Shubham
"""

# PROBLEM STATEMENT 
# Solving for the Energy eigenvalues E of the determinant 
# [ h^2k^2/2m   V_(-2pi/a)              V_(2pi/a)
#   V_(2pi/a)      h^2(k+2pi/a)^2/2m     V_(4pi/a)
#   V_(-2pi/a)     V_(-4pi/a)               h^2(k+2pi/a)^2/2m  ]
# and plotting the Energies for a range of values of k.
# Here, a is the lattice constant and V_G are coeffients in the expansion
# of potential V(x) in the Hamiltonian.
# Note : Read h as huct in the above determinant


# Importing Libraries
import matplotlib.pyplot as plt
import numpy as np


# DEFINING CONSTANTS

h_cut=1;       # We let hcut=6.582*10^(-16) eV.s = 1 unit. This define the scale of our enegy
m=1;           # We let m=1.67*10^(-19) kg = 1 unit 
a=1;           # We let a=1 Angstom = 1 unit as the lattice constant

# Calculating Energy Eigenvalues for a range of values of k 

k=np.linspace(-3.2,3.2,100); # Range of k values where E will be calulated
E_1 = np.zeros(len(k));   # Initializing energy eigenvalues
E_2 = np.zeros(len(k));
E_3 = np.zeros(len(k));

for i in range(1,len(k)):
    # Defining the matrix

    Ea= (h_cut*k[i])**2/2*m;
    Eb= (h_cut*(k[i]+(2*np.pi)/a))**2/2*m;
    Ec= (h_cut*(k[i]-(2*np.pi)/a))**2/2*m;
    V_2=1
    V_4=1
    A = np.array([[Ea,V_2,V_2],[V_2,Eb,V_4],[V_2,V_4,Ec]]);

    # Caculating the energy eigenvalues
    E,v = np.linalg.eig(A);

    # Collecting the energy eigenvalues
    E_1[i] =E[0];
    E_2[i] =E[1];
    E_3[i] =E[2];
    
# Plotting the Energy Eigenvalues 

plt.plot(k,E_2,'.r')
plt.plot(k,E_1,'.b')
plt.plot(k,E_3,'.g')

plt.title('E-k graph')
plt.xlabel('k in pi/a')
plt.ylabel('E in ev')
plt.legend(['E1','E2','E3'])
plt.show()
