#!/bin/bash

for i in {2..12}
do
	cd k_$i
	ener=$(extract_energy.new.sh output)
	echo $i $ener >> ../kpoints.dat
	cd ..
done
