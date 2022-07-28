#!/bin/sh

eventnum=$(grep -A 10 '\"Hoksi Technology KB105\"' /proc/bus/input/devices | grep event | awk -F " " '{print $4}')
#eventnum="event2"
if [ "${#eventnum}" -eq 7 ]
then
	echo "$eventnum" | sed 's/^.*\(.\{2\}\)$/\1/'
else
	echo "$eventnum" | sed 's/^.*\(.\{1\}\)$/\1/'
	#echo "This has 6 char"
fi
