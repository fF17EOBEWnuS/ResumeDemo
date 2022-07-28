#!/bin/sh

. ~/.aliases

if [ $(ps -ef | grep -v grep | grep -v sh | grep barrier | wc -l) -eq 0 ]; then
	sudo -u $User /snap/bin/barrier &
else
	kill -9 `ps -ef | grep barrier | grep -v findkill | grep -v grep | grep -v sh | awk -F " " '{print $2}'`	
	sleep 1
	sudo -u $User /snap/bin/barrier &
fi	


exit 0
