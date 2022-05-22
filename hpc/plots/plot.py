#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


pi=np.pi
r1=np.arange(0.1, 1, 0.001)
r2=0.1
psy12 = 8*(np.exp(-4*r1-2*r2))*(1-2*r2+r2**2)/pi**2
psy21 = 8*(np.exp(-4*r2-2*r1))*(1-2*r1+r1**2)/pi**2

psys=(psy12+psy21)/2**0.5
psya=(psy12-psy21)/2**0.5

plt.xlabel('r1-r2')
plt.ylabel('probability Density')

#plt.title('Symmetric Wavefunction')
plt.title('Antisymmetric Wavefunction')

count=0
while count<100:
	count=count+1
	r2 = r2 +0.01
	psy12 =8*(np.exp(-4*r1-2*r2))*(1-2*r2+r2**2)/pi**2
	psy21 = 8*(np.exp(-4*r2-2*r1))*(1-2*r1+r1**2)/pi**2

	psys=(psy12+psy21)/2**0.5
	psya=(psy12-psy21)/2**0.5

	#plt.scatter(r1-r2,psys**2,s=0.01,color='blue')  #symmetric
	plt.scatter(r1-r2,psya**2,s=0.01,color='red')  #antisymmetric

plt.show()