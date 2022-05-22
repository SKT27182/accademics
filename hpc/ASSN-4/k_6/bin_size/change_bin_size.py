#!/usr/bin/env python3

import os

def replace_data(j):     
        os.chdir("bin_"+str(j))
        #read input file
        fin = open("control.in", "r")
        #read file contents to string
        data = fin.read()
        #replace all occurrences of the required string
        data = data.replace('bin_size', str(j))
        #close the input file
        fin.close()
        #open the input file in write mode
        fin = open("control.in", "w")
        #overrite the input file with the resulting data
        fin.write(data)
        #close the file
        fin.close()
        os.chdir("..")
        print("changed the value of bin_{}".format(j))

for i in (0.05,0.10,0.15):
        replace_data(i)
