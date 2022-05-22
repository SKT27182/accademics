#!/bin/bash

function submit(){
	cd $1
	qsub -qlow aims_sub.sh
	echo Submitted k_$i
	check
}

function check(){
	if [ -f *output* ]
	then
		cd ..
	else
		sleep 1
		check
	fi
}

for i in {2..12}
do
	submit k_$i
done
