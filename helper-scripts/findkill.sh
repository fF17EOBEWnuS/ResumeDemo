#!/bin/bash 

#echo $1

#if [[ $1 -eq "" ]]; then
#	echo "Please enter application search to be killed"
#else
kill -9 `ps -ef | grep $1 | grep -v findkill | grep -v grep | awk -F " " '{print $2}'`
#fi
