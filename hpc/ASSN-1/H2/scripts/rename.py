#!/usr/bin/env python3

import os
#import subprocess
import shutil

#Open a geometry file and then replace the atom2's Z-coordinate to (i/100)
def replace_data(z2):
	os.chdir("run"+str(j))
	#read input file
	fin = open("geometry.in", "r")
	#read file contents to string
	data = fin.read()
	#replace all occurrences of the required string
	data = data.replace('1', str(z2))
	#close the input file
	fin.close()
	#open the input file in write mode
	fin = open("geometry.in", "w")
	#overrite the input file with the resulting data
	fin.write(data)
	#close the file
	fin.close()
	parent_dir = os.path.dirname(os.getcwd())
	os.chdir(parent_dir)
	print("Sucessfully Changed the atom2(z)=" +str(z2))

#Change the current working directory where we want to create the run directories
os.chdir("..")
#Run loop from where you want to start the z coordinate of atom2 in 
for i in range(22, 100):
	j=i-20
	#path = os.getcwd()
	#os.mkdir(path,"run")
	#Check whether the directory exists already or not
	if "run"+str(j) not in os.listdir():
		#copy run1 directory with run(i) name
		shutil.copytree("run1", "run"+str(j), symlinks=False, ignore=None)
		replace_data(i/100)
	else:
		replace_data(i/100)
