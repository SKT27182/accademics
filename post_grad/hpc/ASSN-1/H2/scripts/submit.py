#!/usr/bin/env python3

import os
import subprocess

#change the current location where all the run directories are
os.chdir("..")
dir = os.listdir()

for i in dir:
	if os.path.isdir(i) and i != 'scripts':
		os.chdir(i)
		subprocess.run(['qsub', '-qlow','aims_sub.sh'])
		print("Submitted"+str(i))
		os.chdir('..')
	else:
		pass
