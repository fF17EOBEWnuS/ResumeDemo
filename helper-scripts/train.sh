#!/bin/sh
# Trainer script to 
ext=$1 
counter=1
while true
do
	ls | grep -q $counter
	if [ $? -eq 0 ]
	then 
		counter=$((counter+1))
	else
		break
	fi
done

if [ -z $ext ]; then
	ext=py	
fi

vim $counter.$ext
