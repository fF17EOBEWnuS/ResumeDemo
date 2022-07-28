#!/bin/sh
/usr/bin/notify-send -t 2 "$(echo "Google\n";timeout 2 ping -c 1 google.com | grep ms | head -2)"
