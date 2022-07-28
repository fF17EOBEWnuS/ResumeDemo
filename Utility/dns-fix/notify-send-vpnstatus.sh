#!/bin/sh
/usr/bin/notify-send -t 2 "$(expressvpn status|head -1| sed 's/\x1b\[[0-9;]*m//g')"
