#!/bin/bash

for (( i = 1; i <= 8; i++ )) ### Outer for loop ###
do
	echo $i
	for (( j = 1; j <= 9; j++ ))
	    do
	    echo $j
    	    done
done
