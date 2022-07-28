#!/bin/sh
/usr/bin/notify-send -t 2 "$(echo "Bing\n";timeout 2 ping -c 1 bing.com | grep ms | head -2)"
