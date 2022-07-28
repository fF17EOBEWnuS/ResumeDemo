#!/bin/sh

#notify-send -t 3000 -u normal ""

. ~/.aliases

# Test Ping Connection #

status=$(ping -c 1 www.google.com | grep -c "unknown host")

if [ $status -eq 1 ]; then
       # Connection is bad; need to restart connection	
	nmcli radio wifi off
	sleep 2
	nmcli radio wifi on
	notify-send -t 3000 -u normal ""
	evpnd
fi
