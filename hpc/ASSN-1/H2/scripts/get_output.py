#!/usr/bin/env python3

import re
import os
from array import *
from subprocess import check_output
import matplotlib.pyplot as plt
import numpy as np

array_x = array('f',[])
array_y = array('f',[])



os.chdir("..")
p = r"([0|1][.](([2-9][0-9])|([2-9])))|(1)"



for i in range(2,80):
	dir = "run"+str(i)
	if True:
		os.chdir(dir)
		out = check_output(["extract_energy.new.sh",'output'])
		array_y.append(float(out.decode("utf-8")))
		with open("geometry.in","r") as file:
			for line in file.readlines():
				if re.search(p,line) != None:
					d =re.search(p,line)[0]
					array_x.append(float(re.search(p,line)[0]))
		os.chdir("..")
#print(len(array_x))
#print(len(array_y))

plt.plot(array_x,array_y)
plt.title("Shailja Kant Tiwari-2021PHS7218")
plt.xlabel("bond_length")
plt.ylabel("Energy")
plt.text(0.74,-20,"Equ. B-Length=0.74A")
plt.show()
