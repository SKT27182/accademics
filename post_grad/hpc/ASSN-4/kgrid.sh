#!/bin/bash

function submit(){
	cd $1
	echo "Submitted" #qsub aims_sub.sh
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

for i in {3..12}
do
	submit k_$i
done