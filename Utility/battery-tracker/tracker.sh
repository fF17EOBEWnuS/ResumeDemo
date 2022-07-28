#!/bin/sh

## Battery Tracker for logging battery percentage 

Batpath=$(upower -e | grep battery)

echo $Batpath

curr=$(sudo upower -i $Batpath | grep energy: | awk '{print $2}')
max=$(sudo upower -i $Batpath | grep energy-full: | awk '{print $2}')
#echo $curr
#echo $max

#perc=$(bc << "scale = 10; $curr/$max")
echo $perc






