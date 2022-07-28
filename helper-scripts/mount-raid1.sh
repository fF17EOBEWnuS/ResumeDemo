#!/bin/sh
# only exclusively for mounting Windows Created Software Raid 

sudo mdadm --build --assume-clean /dev/md1 --level=1 --raid-devices=2 /dev/sdc3 /dev/sdd3

