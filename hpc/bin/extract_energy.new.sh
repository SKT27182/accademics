#!/bin/bash
for j1 in $@; do
#cat $1 | while read j1; do
#awk '/Total energy, T -> 0/ {print FILENAME,$0}' $j1 | tail -n 1
#awk '/| Total energy/ || /Total energy corrected/ {print FILENAME,$0}' $j1 | tail -n 6
#awk '/Number of self-consistency cycles/ {printf"%s\t %s\n",FILENAME,$0}' $j1 | tail -n 1
#awk '/Total time            / {printf"%s\t %s\n",FILENAME,$0}' $j1 | tail -n 1
awk '/Total energy corrected/ {printf"%lf\n",$6}' $j1 | tail -n 1
done

