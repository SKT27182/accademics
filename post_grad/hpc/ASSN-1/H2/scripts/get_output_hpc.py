#!/usr/bin/env python3
import re
import os
from array import *
from subprocess import check_output

array_x = array('f',[])
array_y = array('f',[])



os.chdir("..")

p = r"([0-1][.](([2-9][0-9])|([2-9])))|(1)"




#run1 is not executed because after that plot was not good


for i in range(2,80):
	dir = "run"+str(i)
	#print(i)
	if True:
		os.chdir(dir)
		out = check_output(["extract_energy.new.sh",'output'])
		#print(i)
		array_y.append(float(out.decode("utf-8")))
		#print(i)
		with open("geometry.in","r") as file:
			#print(i)
			for line in file.readlines():
				#print(line)
				if re.search(p,line) != None:
					d =re.search(p,line)[0]
					#print(d)
					array_x.append(float(re.search(p,line)[0]))
					#print(array_x)
					#print(i)
		os.chdir("..")
#print(len(array_x))
#print(len(array_y))

for x in range(len(array_x)):
	print(array_x[x],array_y[x])
