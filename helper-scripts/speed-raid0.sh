#!/bin/sh
# only exclusively for mounting Windows Created Software Raid 

#sudo mdadm --assume-clean --build /dev/md0 --level=1 --raid-devices=2 /dev/sdc3 /dev/sdd3
#sudo mdadm --build --assume-clean /dev/md1 --level=1 --raid-devices=2 /dev/sdc3 /dev/sdd3
sudo mdadm -Cv -l0 -c64 -n2 /dev/md1 /dev/sd{c,d}1
