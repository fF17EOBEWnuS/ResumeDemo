#!/usr/bin/python3
"""
Battery tracker in python
"""

import subprocess
#import sys
#import re
from  datetime import datetime, date, time


path = subprocess.check_output("upower -e | grep battery", shell=True)
tpath = str(path.rstrip())[1:]
#print(tpath)
perc = subprocess.check_output("sudo upower -i %s | grep percentage: | awk '{print $2}'" % tpath, shell=True).rstrip()
pperc = perc[:-1]
#curr = float(subprocess.check_output("sudo upower -i %s | grep energy: | awk '{print $2}'" % tpath, shell=True).rstrip())
#maxx = float(subprocess.check_output("sudo upower -i %s | grep energy-full: | awk '{print $2}'" % tpath, shell=True).rstrip())

stamp = datetime.now()
#print(stamp.strftime('[%Y-%m-%d %H:%M:%S]'))
#print(float(pperc))

final = stamp.strftime('[%Y-%m-%d %H:%M:%S] ') + str(float(pperc)) + str('\n')
#print(float(pperc))

f = open('/var/log/battery-percentage.log','a')
f.write(final)
f.close()


