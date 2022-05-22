#!/usr/bin/env python3

import os

def replace_data(j):     
        os.chdir("k_"+str(j))
        #read input file
        fin = open("control.in", "r")
        #read file contents to string
        data = fin.read()
        #replace all occurrences of the required string
        data = data.replace('replace_k', str(j))
        #close the input file
        fin.close()
        #open the input file in write mode
        fin = open("control.in", "w")
        #overrite the input file with the resulting data
        fin.write(data)
        #close the file
        fin.close()
        os.chdir("..")
        print("changed the value of k_{}".format(j))

for i in range(2,13):
        replace_data(i)
